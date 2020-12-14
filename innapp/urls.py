from django.urls import path
from .views import RoomList, BookList, BookingView


app_name = 'innapp'

# one path for each view
urlpatterns = [
    path('room_list/', RoomList.as_view(), name='room_list'),
    path('book_list/', BookList.as_view(), name='book_list'),
    path('book/', BookingView.as_view(), name="booking_view")
]