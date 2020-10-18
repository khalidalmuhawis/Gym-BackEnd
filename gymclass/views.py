from django.shortcuts import render
from .models import Gym, Class, Booking
from django.http import JsonResponse


def gym_list(request):
    gyms = Gym.objects.all()
    return JsonResponse({
        "gyms": [gym.format() for gym in gyms]
    })


def class_list(request):
    classes = Class.objects.all()
    return JsonResponse({
        "classes": [classs.format() for classs in classes]
    })

def booking_list(request):
    bookings = Booking.objects.all()
    return JsonResponse({
        "bookings": [book.format() for book in bookings]
    })
