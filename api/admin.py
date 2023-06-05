from django.contrib import admin
from .models import *


class AvailabilityInline(admin.TabularInline):
    fk_name = 'room'
    model = Availability
    extra = 0


class BookingInline(admin.TabularInline):
    fk_name = 'room'
    model = Booking
    extra = 0


class RoomAdmin(admin.ModelAdmin):
    fields = ["name", "type", "capacity"]
    inlines = [AvailabilityInline, BookingInline]


# Register your models here.
admin.site.register(Room, RoomAdmin)
admin.site.register(Resident)
