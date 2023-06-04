from django.shortcuts import get_object_or_404

from .models import Room, Availability


def get_rooms_list(search=None, type=None):
    """ This service returns all rooms """
    if not search and not type:
        return Room.objects.all()
    if not search and type:
        return Room.objects.filter(type=type)
    if search and not type:
        return Room.objects.filter(name__icontains=search)


def get_rooms_detail(pk):
    """ This service returns exact room using pk """
    return get_object_or_404(Room, pk=pk)


def get_rooms_detail_availability(pk, date=None):
    """ This service returns available times for particular room """
    if not date:
        return Availability.objects.filter(room__pk=pk)
    return Availability.objects.filter(room__pk=pk, date=date)
