from datetime import datetime
from tests.config import ENDPOINT
import requests

from tests.services import new_booking_payload, create_booking, get_booking, get_list_bookings, get_list_rooms, \
    get_list_availability


def test_can_call_endpoint():
    """ This test checks if the request can reach out the root API endpoint """
    response = requests.get(ENDPOINT)
    assert response.status_code == 200


def test_can_book_room():
    """ This test creates booking and checks its status and if all the information match (id, date, start_time,
    end_time)"""
    payload = new_booking_payload()
    create_booking_response = create_booking(payload)
    assert create_booking_response.status_code == 201

    """ Checking the id """
    data = create_booking_response.json()
    print(data)
    booking_id = data['booking_id']
    get_booking_response = get_booking(booking_id)

    assert get_booking_response.status_code == 200

    """ Checking the other information """
    get_booking_data = get_booking_response.json()

    payload_date, payload_start_time = payload["start"].split(" ")
    payload_end_time = payload["end"].split(" ")[1]

    assert datetime.strptime(get_booking_data["date"], '%Y-%m-%d').date() == datetime.strptime(payload_date,
                                                                                               '%Y-%m-%d').date()
    assert datetime.strptime(get_booking_data["start"], '%H:%M:%S') == datetime.strptime(payload_start_time, '%H:%M:%S')
    assert datetime.strptime(get_booking_data["end"], '%H:%M:%S') == datetime.strptime(payload_end_time, '%H:%M:%S')
    assert get_booking_data["resident"]["name"] == payload["resident"]["name"]


def test_can_list_bookings():
    """ This test gets the list of bookings and checks the status """
    list_booking_response = get_list_bookings()
    assert list_booking_response.status_code == 200
    data = list_booking_response.json()
    print(data)


def test_can_list_rooms():
    """ This test gets the list of rooms and checks the status """
    list_room_response = get_list_rooms()
    assert list_room_response.status_code == 200


def test_can_list_availability():
    """ This test gets the list of availabilities and checks the status """
    list_availability_response = get_list_availability()
    assert list_availability_response.status_code == 200
