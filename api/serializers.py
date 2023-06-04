from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Room, Availability


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'name', 'type', 'capacity')
        depth = 1


class AvailabilitySerializer(ModelSerializer):
    start = SerializerMethodField()
    end = SerializerMethodField()

    class Meta:
        model = Availability
        fields = ('start', 'end')

    def get_start(self, obj):
        return '{} {}'.format(obj.date, obj.start)

    def get_end(self, obj):
        return '{} {}'.format(obj.date, obj.end)
