from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Room(models.Model):
    # cu baie, fara baie
    ROOM_CATEGORIES = ( ('WB', 'bathroom'), ('NB', 'nbathroom'))
    number = models.IntegerField(default=0)
    category = models.CharField(max_length=5, choices=ROOM_CATEGORIES)
    beds = models.IntegerField(default=0)
    capacity = models.IntegerField(default=0)

    def __str__(self):
        return 'Room No. {} with {} and {} number of beds.'.format(self.number, self.category, self.beds)

class Book(models.Model):
    # many to one relationship, https://docs.djangoproject.com/en/3.1/ref/models/fields/
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    number_of_rooms = models.IntegerField(default=0)

    def __str__(self):
        return 'Client {} has booked {} rooms {} on {} to {}'.format(self.client, self.number_of_rooms, self.room, self.check_in, self.check_out)




class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(default="+407...", max_length=50)
