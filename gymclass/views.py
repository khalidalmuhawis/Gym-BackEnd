from django.shortcuts import render
from .models import Gym, Class, Booking
from django.http import JsonResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET', 'POST'])
def gym_list(request):
    if request.method == 'GET':
        data = Gym.objects.all()
        serializer = GymSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':

        name = request.data.get("name", None)
        openningtime = request.data.get('openningtime', None)
        closingtime = request.data.get('closingtime', None)
        image = request.data.get('image', None)
        new_gym= Gym(name=name, openningtime=openningtime, closingtime=closingtime, image=image)

        try:
            new_gym.save()
            return JsonResponse({'status': 1, 'message': 'Your profile updated successfully!'})
        except:
            return JsonResponse({'status': 0, 'message': 'There was something wrong while updating your profile.'})


def class_list(request):
    gym=Gym.objects.get(id=1)
    classes = Class.objects.filter(gym=gym)
    return JsonResponse({
        "classes": [classs.format() for classs in classes]
    })

def booking_list(request):
    bookings = Booking.objects.all()
    return JsonResponse({
        "bookings": [book.format() for book in bookings]
    })
