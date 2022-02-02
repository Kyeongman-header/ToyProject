from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from django.conf.urls import include
from . import views

router=routers.DefaultRouter()
router.register(r'user',views.UserViewSet)
router.register(r'image',views.ImageViewSet)
router.register(r'points',views.PointsViewSet)


urlpatterns=[
    path('',views.index,name='index'),    
    path('api/',include(router.urls)),
]
