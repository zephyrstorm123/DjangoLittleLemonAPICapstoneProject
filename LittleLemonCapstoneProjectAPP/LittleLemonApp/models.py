from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=50)
    number_of_guests = models.IntegerField(default=1)
    Booking_date = models.DateField()

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(default=1)


    def __str__(self):
        return self.name