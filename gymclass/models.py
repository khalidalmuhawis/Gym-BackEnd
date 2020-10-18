from django.db import models
from django.contrib.auth.models import User


class Gym(models.Model):
    name = models.CharField(max_length=100)
    openningtime = models.TimeField()
    closingtime = models.TimeField()
    image = models.ImageField()

    def format(self):
        return {
          'id': self.id,
          'name': self.name,
          'openningtime': self.openningtime,
          'closingtime': self.closingtime,
          'image': self.image.url
        }

    def __str__(self):
        return "%s" % (self.name)


class Class(models.Model):
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE, related_name="classes")
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    isFree = models.BooleanField()

    def format(self):
        return {
          'id': self.id,
          'gym': self.gym.name,
          'title': self.title,
          'type': self.type,
          'datetime': self.datetime,
          'isFree': self.isFree
        }

    def __str__(self):
        return "%s" % (self.title)

class Booking(models.Model):
    classes = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="bookings")
    guest = models.ForeignKey(User, on_delete=models.CASCADE, related_name='guest')


    def format(self):
        return {
          'id': self.id,
          'classes': self.classes.title,
          'classtime':self.classes.datetime,
          'guest': self.guest.username
        }

    def __str__(self):
        return self.classes.title
