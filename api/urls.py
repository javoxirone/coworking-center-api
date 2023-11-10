from django.urls import path
from .views import api_root, rooms_list_api_view, rooms_detail_api_view, rooms_detail_availability_api_view, \
    rooms_book_api_view, bookings_detail_api_view, bookings_list_api_view

urlpatterns = [
    path("", api_root, name="api_root"),
    path("rooms/", rooms_list_api_view, name="rooms-list"),
    path("rooms/<int:pk>/", rooms_detail_api_view, name="rooms-detail"),
    path("rooms/<int:pk>/availability/", rooms_detail_availability_api_view, name="rooms-detail-availability"),
    path("rooms/<int:pk>/book/", rooms_book_api_view, name="rooms-book"),

    path("bookings/<int:pk>/", bookings_detail_api_view, name="bookings-detail"),
    path("bookings/", bookings_list_api_view, name="bookings-list"),
]