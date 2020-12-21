from django.shortcuts import render, HttpResponse, reverse, redirect 
from django.views.generic import ListView, FormView, View, CreateView, TemplateView, UpdateView, DetailView
from .models import Room, Book, User, ClientProfile
from .forms import AvailibiltyForm, ProfileForm


from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


def check_if_available(room, start_date, end_date):
        """
        Checks if a room is available at a given period
        """
        timeline = []

        # gets all the reservations of the room from the database
        bookings_of_the_room = Book.objects.filter(room = room)

        for b in bookings_of_the_room:
            # checks if the start date is already in a booked interval
            if start_date >= b.check_in and start_date < b.check_out:
                return False

            # same for the end date
            if end_date > b.check_in and end_date <= b.check_out:
                return False 

        return True





# Create your views here.
def RoomListView(request):
    # gets the first room
    room = Room.objects.all()[0]
    room_category= dict(room.ROOM_CATEGORIES)
    # print(reverse('innapp:room_view', kwargs={'cateogory': 'WB'}))
    room_values = room_category.values()
    room_list = []
    for r in room_category:
        room = room_category.get(r)
        # primul argument e numele ddin urls.py https://www.youtube.com/watch?v=JqbBGxDLQeU
        room_url = reverse('innapp:room_view', kwargs={
                           'category': r})
        room_list.append((r, room_url))

    context = {
        "room_list":room_list
    }
    return render (request, 'innapp/room_list.html', context=context)

class RoomView(View):
    def get(self, request, *args, **kwargs):
        # print(self.request.user)
        return HttpResponse('Category does not exist')

class MainView(View):
    def get(self, request, *args, **kwargs):
        """
        docstring
        """
        return render(request, "main_view.html")

class Booked(View):
    def get(self, request, *args, **kwargs):
        """
        docstring
        """
        return render(request, "booked.html")


class BookList(ListView):
    model = Book

class BookingView(FormView):
    form_class = AvailibiltyForm
    template_name = 'availibility_form.html'

    

    def form_valid(self, form):
        data = form.cleaned_data
        # print(data['room_category'])
        room_list = Room.objects.filter(category=data['room_category'])
        # print("!!!! rooms list", room_list)
        available_rooms = []

        for room in room_list:
            if check_if_available(room, data['check_in'], data['check_out']):
                available_rooms.append(room)

        number_of_availbale_rooms = len(available_rooms)
        print(number_of_availbale_rooms )

        if number_of_availbale_rooms > 0:

            # take the first room available
            room = available_rooms[0]
            book = Book.objects.create(
                client = self.request.user,
                room = room,
                check_in = data['check_in'],
                check_out= data['check_out'], 
                number_of_rooms=data['number_of_rooms']
            )

            book.save()
            return redirect("/booked")
        else:
            # return HttpResponse('There are no rooms for this category available.')
            return HttpResponse("There are no available rooms for this period. Please choose another one!")



class RegisterView(CreateView):
    template_name= 'register.html'
    form_class = UserCreationForm
    model = User

    def form_valid(self, form):
        data = form.cleaned_data
        user = User.objects.create_user(username=data['username'],
                                        password=data['password1'])
        ClientProfile.objects.create(user=user)
        return redirect('/login')



class LoginView(TemplateView):
    template_name = 'login.html'

    def get_context_data(self):
        form = AuthenticationForm()
        return {'form': form}

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'],
                                password=data['password'])
            login(request, user)
            return redirect('/')
        else:
            return render(request, "login.html", {"form": form})


def logout_r(request):
    logout(request)
    return redirect("/")

class ProfileView(DetailView):
    template_name = 'profile.html'
    context_object_name = 'selected_user'

    def get_object(self):
        selected_user = User.objects.get(id=self.kwargs['pk'])
        return selected_user


class ProfileUpdateView(UpdateView):
    model = ClientProfile
    form_class = ProfileForm
    template_name = 'profile_update.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileUpdateView, self).get_context_data(**kwargs)
        user =  self.object.user
        context['form'].fields['first_name'].initial = user.first_name
        print(user.first_name)
        print(user.last_name)

        context['form'].fields['last_name'].initial = user.last_name
        context['form'].fields['email'].initial = user.email
        return context

    def form_valid(self, form):
        data = form.cleaned_data
        self.object.phone_number = data['phone_number']
        self.object.address = data['address']
        self.request.user.first_name = data['first_name']
        self.request.user.last_name = data['last_name']
        self.request.user.email = data['email']
        self.object.save()
        self.request.user.save()
        return redirect("/",kwargs={"pk": self.request.user.id})