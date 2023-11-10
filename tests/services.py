import requests
from tests.config import ENDPOINT


def create_booking(payload):
    """ This service sends post request to the booking API endpoint """
    return requests.post(ENDPOINT + "/rooms/1/book/", json=payload)


def get_booking(booking_id):
    """ This service sends get request to bookings detail API endpoint """
    return requests.get(ENDPOINT + f"/bookings/{booking_id}/")


def get_list_bookings():
    """ This service sends get request to bookings API endpoint """
    return requests.get(ENDPOINT + f"/bookings/")


def get_list_rooms():
    """ This service sends get request to rooms API endpoint """
    return requests.get(ENDPOINT + f"/rooms/")


def get_list_availability():
    """ This service sends get request to availability API endpoint """
    return requests.get(ENDPOINT + f"/rooms/1/availability/")


def new_booking_payload():
    """ This service returns the json object for testing """
    return {
        "resident":
            {
                "name": "Javohir Nurmatjonov"
            },
        "start": "2024-06-14 15:10:00",
        "end": "2024-06-14 15:11:00"
    }
