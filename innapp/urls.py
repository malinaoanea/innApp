from django.urls import path
from .views import RoomListView, BookList, BookingView, MainView, RoomView, RegisterView, LoginView, index, ProfileUpdateView,ProfileView , logout_r, Booked


app_name = 'innapp'

# one path for each view
urlpatterns = [
    path('room_list/', RoomListView, name='room_list'),
    path('book_list/', BookList.as_view(), name='book_list'),
    path('book/', BookingView.as_view(), name="booking_view"),
    path('', MainView.as_view(), name="home"),
    path('room_view/<category>', RoomView.as_view(), name="room_view"),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/',logout_r,name='logout'),

    # path('profile_update', ProfileUpdateView.as_view(), name='profile_update'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('reservation_history/', index, name='reservation_history'),

    path('profile_update/<int:pk>', ProfileUpdateView.as_view(), name='profile_update'),
    path('booked', Booked.as_view(), name='booked')
]

# urlpatterns += statcfiles_urlpatterns()