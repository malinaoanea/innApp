from django.urls import path
from .views import RoomListView, BookList, BookingView, MainView, RoomView, RegisterView, LoginView


app_name = 'innapp'

# one path for each view
urlpatterns = [
    path('room_list/', RoomListView, name='room_list'),
    path('book_list/', BookList.as_view(), name='book_list'),
    path('book/', BookingView.as_view(), name="booking_view"),
    path('home/', MainView.as_view(), name="home"),
    path('room_view/<category>', RoomView.as_view(), name="room_view"),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login')

]

# urlpatterns += statcfiles_urlpatterns()