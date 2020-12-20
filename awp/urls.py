"""awp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from innapp.views import RoomListView, BookList, BookingView, MainView, RoomView, RegisterView, LoginView,ProfileView, ProfileUpdateView, logout_r


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('innapp.urls')),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),

    path('profile_update/<int:pk>', ProfileUpdateView.as_view(), name='profile_update')
]
