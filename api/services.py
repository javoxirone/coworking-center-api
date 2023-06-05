from django.shortcuts import get_object_or_404
from .models import Room, Availability, Resident
from datetime import datetime, timedelta


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


def get_resident_or_create(name):
    try:
        resident = Resident.objects.get(name=name)
    except Exception as e:
        print(e)
        resident = Resident(name=name)
        resident.save()
    return resident


def _get_time_difference_formatted(time1, time2):
    """ This service returns time difference between two times (private) """
    delta = datetime.strptime(str(time1), '%H:%M:%S') - datetime.strptime(str(time2), '%H:%M:%S')
    return str(delta)


def _get_time_sum_formatted(time1, time2):
    """ This service returns the sum of two times (private) """
    result_time = datetime.combine(datetime.today(), datetime.strptime(time1, '%H:%M:%S').time()) + timedelta(
        hours=time2.hour, minutes=time2.minute, seconds=time2.second)
    return str(result_time).split(" ")[1]


def get_new_time_slots(start_time, end_time, available_time_slot):
    diff_end = _get_time_difference_formatted(available_time_slot.end, end_time)
    diff_start = _get_time_difference_formatted(start_time, available_time_slot.start)

    new_start_1 = datetime.strptime(str(available_time_slot.start), '%H:%M:%S')
    new_end_1 = datetime.strptime(_get_time_sum_formatted(diff_start, available_time_slot.start), '%H:%M:%S')
    new_start_2 = datetime.strptime(_get_time_difference_formatted(available_time_slot.end, diff_end), '%H:%M:%S')
    new_end_2 = datetime.strptime(str(available_time_slot.end), '%H:%M:%S')

    return (new_start_1, new_end_1), (new_start_2, new_end_2)
