"""Gym URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from gymclass import views
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('gyms/', views.GymList.as_view(), name='gym-list'),
    path('gyms/create/', views.GymCreate.as_view(), name='gym-create'),
    path('gyms/<int:gym_id>/', views.class_list, name='gyms-list'),
    path('classes/<str:class_type>/', views.class_list_byType, name='classes-type'),
    path('classes/<int:class_id>/detail/', views.ClassDetail.as_view(), name='classes-detail'),
    path('classes/<int:gym_id>/create/', views.ClassCreate.as_view(), name='classes-create'),
    path('bookings/', views.booking_list, name='bookings-list'),
    path('bookings/<int:class_id>/create/', views.BookClass.as_view(), name='book-class'),

    # auth links
    path('signin/', TokenObtainPairView.as_view(), name="api-signin"),
    path('signup/', views.Register.as_view(), name="api-signup"),

]

if settings.DEBUG:
    '''Uncomment the next line to include your static files'''
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
