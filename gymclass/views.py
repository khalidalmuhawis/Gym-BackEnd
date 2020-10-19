from django.shortcuts import render
from .models import Gym, Class, Booking
from django.http import JsonResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser



# @api_view(['GET', 'POST'])
# def gym_list(request):
#     if request.method == 'GET':
#         data = Gym.objects.all()
#         serializer = GymSerializer(data, context={'request': request}, many=True)

#         return Response(serializer.data)

#     elif request.method == 'POST':

#         name = request.data.get("name", None)
#         openningtime = request.data.get('openningtime', None)
#         closingtime = request.data.get('closingtime', None)
#         image = request.data.get('image', None)
#         new_gym= Gym(name=name, openningtime=openningtime, closingtime=closingtime, image=image)

#         try:
#             new_gym.save()
#             return JsonResponse({'status': 1, 'message': 'Your profile updated successfully!'})
#         except:
#             return JsonResponse({'status': 0, 'message': 'There was something wrong while updating your profile.'})

class GymList(ListAPIView):
	serializer_class = GymSerializer
	permission_classes = [IsAuthenticated]

	def get_queryset(self):
		return Gym.objects.all()

# class ClassList(RetrieveAPIView):
# 	queryset = Class.objects.all()
# 	serializer_class = ClassSerializer
# 	lookup_field = 'id'
# 	lookup_url_kwarg = 'gym_id'
# 	permission_classes = [AllowAny]

class GymCreate(CreateAPIView):
	serializer_class = GymSerializer
	permission_classes = [IsAuthenticated, IsAdminUser]

class ClassCreate(CreateAPIView):
	serializer_class = ClassSerializer
	permission_classes = [IsAuthenticated, IsAdminUser]

	def perform_create(self, serializer):
		serializer.save(gym_id=self.kwargs['gym_id'])

def class_list(request, gym_id):
    gym=Gym.objects.get(id=gym_id)
    classes = Class.objects.filter(gym=gym)
    return JsonResponse({
        "classes": [classs.format() for classs in classes]
    })

def class_list_byType(request, class_type):
    classes = Class.objects.filter(class_type=class_type)
    return JsonResponse({
        "classes": [classs.format() for classs in classes]
    })


def booking_list(request):
    bookings = Booking.objects.all()
    return JsonResponse({
        "bookings": [book.format() for book in bookings]
    })

class Register(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

class ClassDetail(RetrieveAPIView):
	queryset = Class.objects.all()
	serializer_class = ClassDetailsSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'class_id'
	permission_classes = [AllowAny]


class BookClass(CreateAPIView):
    serializer_class = BookingSerializer
    # permission_classes = [AllowAny]
    
    def perform_create(self, serializer):
        class_obj = Class.objects.get(id=self.kwargs['class_id'])
        serializer.save(guest=self.request.user, classes=class_obj)
