from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView, View
from .models import Room, Book
from .forms import AvailibiltyForm

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
class RoomList(ListView):
    model = Room

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

