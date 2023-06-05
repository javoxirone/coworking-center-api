from django.db import models


# Create your models here.
class Room(models.Model):
    TYPE_CHOICES = (
        ("focus", "Focus"),
        ("team", "Team"),
        ("conference", "Conference"),
    )

    CAPACITY_CHOICES = (
        (15, 15),
        (5, 5),
        (1, 1),
    )

    name = models.CharField(max_length=255, unique=True, null=False, blank=False, verbose_name="Name")
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, null=False, blank=False,
                            verbose_name="Type of the room")
    capacity = models.IntegerField(choices=CAPACITY_CHOICES, null=False, blank=False,
                                   verbose_name="Capacity of the room")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Room(name={self.name}, type={self.type})"


class Resident(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, blank=False, verbose_name="Name of the resident")

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Resident(name={self.name})"


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Room",
                             related_name="bookings")
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Resident",
                                 related_name="bookings")
    date = models.DateField(default=None, null=True, blank=True, verbose_name="Date")
    start = models.TimeField(null=False, blank=False, verbose_name="Start time")
    end = models.TimeField(null=False, blank=False, verbose_name="End time")

    def __str__(self):
        return self.resident.name

    def __repr__(self):
        return f"Booking(room={self.room.name}, resident={self.resident.name}, start={self.start}, end={self.end})"


class Availability(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Room",
                             related_name="available_times")
    date = models.DateField(default=None, null=True, blank=True, verbose_name="Date")
    start = models.TimeField(null=False, blank=False, verbose_name="Start time")
    end = models.TimeField(null=False, blank=False, verbose_name="End time")

    def __str__(self):
        return self.room.name

    def __repr__(self):
        return f"Availability(room={self.room.name}, start={self.start}, end={self.end})"

    class Meta:
        verbose_name = "Available time"
        verbose_name_plural = "Available times"
