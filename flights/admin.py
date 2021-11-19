from django.contrib import admin

from .models import Flight, Airport, Passenger

# Register your models here.
# these tell Django's admin app that I want to manipulate Airports and Flights models
class FlightAdmin(admin.ModelAdmin):
    list_display = ("origin", "destination", "duration") # look up django doco for 'list_display'

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",) #filter_horizontal another django configurable setting

admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)