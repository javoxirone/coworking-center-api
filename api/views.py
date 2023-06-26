from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Booking
from .services import get_rooms_list, get_rooms_detail, get_rooms_detail_availability, get_list_or_object_of_booking, \
    check_and_convert_date
from .serializers import RoomSerializer, AvailabilitySerializer, BookingCreateSerializer, BookingSerializer


# Create your views here.

@api_view(['GET'])
def api_root(request):
    """
    This view returns a list of the available API endpoints.
    """
    return Response({
        'rooms/': reverse('rooms-list', request=request),
    })


@api_view(['GET'])
def rooms_list_api_view(request):
    """ This view returns the list of rooms """
    page = request.GET.get('page', 1),
    page_size = request.GET.get('page_size', 10)
    search = request.GET.get('search', None)
    type = request.GET.get('type', None)
    queryset = get_rooms_list(search, type)
    count = queryset.count()

    paginator = PageNumberPagination()
    paginator.page_size = page_size

    result_page = paginator.paginate_queryset(queryset, request)
    serializer = RoomSerializer(result_page, many=True)
    context = {
        'page': int(page[0]),
        'count': count,
        'page_size': int(paginator.page_size),
        'results': serializer.data,
    }
    return Response(context, status=status.HTTP_200_OK)


# TODO: review this code, and maybe rewrite in more clear way
@api_view(['GET'])
def rooms_detail_api_view(request, pk):
    """ This view returns single room, otherwise returns custom error """
    try:
        room = get_rooms_detail(pk)
        serializer = RoomSerializer(room, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({"error": "topilmadi"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def rooms_detail_availability_api_view(request, pk):
    """ This view returns particular room available times """
    date = request.GET.get("date", None)
    date = check_and_convert_date(date)

    available_times = get_rooms_detail_availability(pk, date)
    serializer = AvailabilitySerializer(available_times, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def rooms_book_api_view(request, pk):
    """ This view creates new booking and returns the custom message with 201 status if it successfully created,
    otherwise it returns list of errors that happened during validation"""
    room = get_rooms_detail(pk)
    serializer = BookingCreateSerializer(data=request.data, context={"room": room})  # we can pass that here using context attr.
    if serializer.is_valid():
        booking = serializer.save()  # passing context here
        return Response({"message": "xona muvaffaqiyatli band qilindi", "booking_id": booking.pk},
                        status=status.HTTP_201_CREATED)
    return Response({"error": "uzr, siz tanlagan vaqtda xona band"}, status=status.HTTP_410_GONE)


# TODO: test the built rest api


@api_view(['GET'])
def bookings_detail_api_view(request, pk):
    """ This view returns single booking as a response """
    booking = get_list_or_object_of_booking(pk=pk)
    serializer = BookingSerializer(booking, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def bookings_list_api_view(request):
    bookings = get_list_or_object_of_booking()
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
