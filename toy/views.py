from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.viewsets import ReadOnlyModelViewSet,ModelViewSet
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django.core import serializers
from django_filters.rest_framework import DjangoFilterBackend 
from django_filters import FilterSet,DateTimeFilter,ModelChoiceFilter

from django.contrib.auth import get_user_model
from .models import *
from .serializers import *


# Create your views here.

def index(request):
    return HttpResponse("Toy Project")

class ImageFilter(FilterSet):
    pub_date__gte=DateTimeFilter(field_name="pub_date",lookup_expr='gte')
    pub_date__lte=DateTimeFilter(field_name="pub_date",lookup_expr='lte')
    user=ModelChoiceFilter(field_name="user",queryset=get_user_model().objects.all())
    class Meta:
        model=Image
        fields=['pub_date__gte','pub_date__lte','user']


class ImageViewSet(ModelViewSet):
    queryset=Image.objects.all()
    serializer_class=ImageSerializer
    permission_classes=[AllowAny]#IsAuthenticated
    #authentication_classes=[TokenAuthentication]
    filter_backends=(DjangoFilterBackend,)
    filter_class=ImageFilter

class UserViewSet(ReadOnlyModelViewSet):
    serializer_class=UserSerializer
    queryset=get_user_model().objects.all()
    permission_classes=[IsAdminUser]
    #authentication_classes=[TokenAuthentication]

class PointsFilter(FilterSet):
    pub_date__gte=DateTimeFilter(field_name="pub_date",lookup_expr='gte')
    pub_date__lte=DateTimeFilter(field_name="pub_date",lookup_expr="lte")
    user=ModelChoiceFilter(field_name="user",queryset=get_user_model().objects.all())
    class Meta:
        model=Points
        fields=['pub_date__gte','pub_date__lte','user']


class PointsViewSet(ModelViewSet):
    queryset=Points.objects.all()
    serializer_class=PointsSerializer
    permission_classes=[AllowAny]
    filter_backends=(DjangoFilterBackend,)
    filter_class=PointsFilter


    



