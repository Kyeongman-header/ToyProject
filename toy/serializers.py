from django.contrib.auth.models import User
from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','groups']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Image
        fields=['user','screenshot','title','pub_date']

class PointsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Points
        fields=['user','point_one','point_two','point_three','pub_date']

