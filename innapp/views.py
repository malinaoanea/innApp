from django.shortcuts import render, HttpResponse, reverse, redirect
from django.views.generic import ListView, FormView, View, CreateView, TemplateView
from .models import Room, Book, User, Client
from .forms import AvailibiltyForm, RegisterForm


from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout


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

        if len(available_rooms) > 0:

            # take the first room available
            room = available_rooms[0]
            book = Book.objects.create(
                client = self.request.user,
                room = room,
                check_in = data['check_in'],
                check_out= data['check_out']
            )

            book.save()
            return HttpResponse(book)
        else:
            return HttpResponse('There are no rooms for this category available.')


class RegisterView(CreateView):
    template_name= 'register.html'
    form_class = RegisterForm
    model = User

    def form_valid(self, form):
        data = form.cleaned_data
        user = User.objects.create_user(username=data['username'],
                                        password=data['password1'])
        Client.objects.create(user=user)
        return redirect('/')



class LoginView(TemplateView):
    template_name = 'login.html'

    def get_context_data(self):
        form = AuthenticationForm()
        return {'form':form}

    def post(self, request, *args, **kargs):
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'],
                                password=data['password'])
            if user is not None:
                login(request, user)
                return redirect('/')
            else:

                return render(request, "login.html", {"form":form}, status = "unsucces")

        else:
            return render(request, "login.html", {"form":form})


def logout_r(request):
    logout(request)
    return redirect("register")