from django.db import models
from django.conf import settings

# Create your models here.

class Room(models.Model):
    # cu baie, fara baie
    ROOM_CATEGORIES = ( ('WB', 'bathroom'), ('NB', 'no bathroom'))
    number = models.IntegerField(default=0)
    category = models.CharField(max_length=5, choices=ROOM_CATEGORIES)
    beds = models.IntegerField(default=0)
    capacity = models.IntegerField(default=0)

    def __str__(self):
        return 'Room No. {} with {} and {} number of beds.'.format(self.number, self.category, self.beds)

class Client(models.Model):
    first_name = models.CharField(default="First Name", max_length=50)
    last_name = models.CharField(default="Last Name", max_length=50)

    email = models.CharField(default="email@email.com", max_length=50)
    phone_number = models.CharField(default="+407...", max_length=50)

class Book(models.Model):
    # many to one relationship, https://docs.djangoproject.com/en/3.1/ref/models/fields/
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return 'Client {} has booked room {} on {} to {}'.format(self.client, self.room, self.check_in, self.check_out)


