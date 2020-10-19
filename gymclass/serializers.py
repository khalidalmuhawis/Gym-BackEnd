from rest_framework import serializers
from .models import Gym, Class
from django.contrib.auth.models import User

class GymSerializer(serializers.ModelSerializer):
  class Meta:
    model = Gym
    fields = ('id','name', 'openningtime', 'closingtime', 'image')

          # 'id': self.id,
          # 'gym': self.gym.name,
          # 'title': self.title,
          # 'type': self.type,
          # 'datetime': self.datetime,
          # 'isFree': self.isFree

class ClassSerializer(serializers.ModelSerializer):
  class Meta:
    model = Class
    fields = ('id','title', 'class_type', 'datetime', 'isFree')


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'password', 'email', 'is_staff']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        if validated_data['is_staff']:
          new_user = User(username=username, first_name=first_name, last_name=last_name, email=email, is_staff=True)
        else:
          new_user = User(username=username, first_name=first_name, last_name=last_name, email=email)
        new_user.set_password(password)
        new_user.save()
        return validated_data
