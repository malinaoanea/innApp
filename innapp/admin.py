from django.contrib import admin
from .models import Room, Book, ClientProfile

# Register your models here.
admin.site.register(Room)
admin.site.register(Book)
admin.site.register(ClientProfile)
