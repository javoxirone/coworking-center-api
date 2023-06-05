from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import Room, Availability, Booking, Resident
from .services import get_resident_or_create, get_new_time_slots


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'name', 'type', 'capacity')
        depth = 1


class AvailabilitySerializer(serializers.ModelSerializer):
    start = serializers.SerializerMethodField()
    end = serializers.SerializerMethodField()

    class Meta:
        model = Availability
        fields = ('start', 'end')

    def get_start(self, obj):
        return '{} {}'.format(obj.date, obj.start)

    def get_end(self, obj):
        return '{} {}'.format(obj.date, obj.end)


class BookingSerializer(serializers.Serializer):
    resident = serializers.DictField(child=serializers.CharField())
    start = serializers.CharField()
    end = serializers.CharField()

    def validate(self, data):
        date, start_time = data['start'].split(" ")
        end_time = data['end'].split(" ")[1]
        room = self.context['room']
        overlapping_bookings = room.bookings.filter(date=date, start__lt=end_time, end__gt=start_time)
        overlapping_availabilities = room.available_times.filter(date=date, start__lt=end_time, end__gt=start_time)
        if overlapping_bookings.exists() or not overlapping_availabilities:
            raise serializers.ValidationError({"error": "uzr, siz tanlagan vaqtda xona band"})
        return data

    def create(self, validated_data):
        room = self.context['room']
        resident_name = validated_data['resident']['name']
        date, start_time = validated_data['start'].split(" ")
        end_time = validated_data['end'].split(" ")[1]
        available_time_slot = room.available_times.get(start__lt=end_time, end__gt=start_time)
        new_time_slots = get_new_time_slots(start_time, end_time, available_time_slot)
        available_time_slot.delete()

        for time_slot in new_time_slots:
            start = time_slot[0]
            end = time_slot[1]
            print(start, end)
            if start == end:
                continue
            available_time = Availability(room=room, date=date, start=start, end=end)
            available_time.save()

        resident = get_resident_or_create(resident_name)
        booking = Booking(room=room, resident=resident, date=date, start=start_time, end=end_time)
        booking.save()
        return booking


