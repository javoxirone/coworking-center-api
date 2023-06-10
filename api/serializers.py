from datetime import datetime, date

from rest_framework import serializers
from .models import Room, Availability
from .services import get_resident_or_create, get_new_time_slots, get_overlapping_bookings_list, \
    get_overlapping_availabilities_list, get_available_time_slot, create_two_time_slots, create_new_booking


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
        date_str, start_time = data['start'].split(" ")
        end_time = data['end'].split(" ")[1]

        room = self.context['room']
        overlapping_bookings = get_overlapping_bookings_list(room, date_str, start_time, end_time)
        overlapping_availabilities = get_overlapping_availabilities_list(room, date_str, start_time, end_time)
        if overlapping_bookings.exists() or not overlapping_availabilities:
            raise serializers.ValidationError({"error": "uzr, siz tanlagan vaqtda xona band"})
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
        current_date = date.today()
        if date_obj < current_date:
            raise serializers.ValidationError({"error": "o'tgan zamonga xona band qilolmaysiz =)"})
        return data

    def create(self, validated_data):
        room = self.context['room']
        resident_name = validated_data['resident']['name']
        date, start_time = validated_data['start'].split(" ")
        end_time = validated_data['end'].split(" ")[1]
        available_time_slot = get_available_time_slot(room, start_time, end_time)
        new_time_slots = get_new_time_slots(start_time, end_time, available_time_slot)
        available_time_slot.delete()
        create_two_time_slots(new_time_slots, room, date)
        resident = get_resident_or_create(resident_name)
        booking = create_new_booking(room, resident, date, start_time, end_time)
        return booking
