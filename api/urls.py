from django.urls import path
from .views import api_root, rooms_list_api_view, rooms_detail_api_view, rooms_detail_availability_api_view

urlpatterns = [
    path("", api_root, name="api_root"),
    path("rooms/", rooms_list_api_view, name="rooms-list"),
    path("rooms/<int:pk>/", rooms_detail_api_view, name="rooms-detail"),
    path("rooms/<int:pk>/availability/", rooms_detail_availability_api_view, name="rooms-detail-availability")
]