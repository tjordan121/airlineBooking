from math import degrees
from django.db import models

# Create your models here.
# each model will be a class. THin of each class as being one model for each of the main tables we store info for
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures") # models.CASCADE means if an Airport is deleted from Airports table it will also delete corresponding flights. - related_name: access relationship in reverse order. Find flights that have airport as origin
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self): # return a string representation of this particular object
        return f"{self.id}: {self.origin} to {self.destination}"

    def is_valid_flight(self):
        return self.origin != self.destination and self.duration > 0

class Passenger(models.Model): # A passenger is many-to-many with flights but can also have zero (blank) flights
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank = True, related_name="passengers")

    def __str__(self): # This creates a string representation of a 'Passenger'
        return f"{self.first} {self.last}"
