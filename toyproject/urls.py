"""toyproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.conf.urls import url
from django.contrib import admin
from django.urls import include,path
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',include('toy.urls')),
    path('api-token-auth/',obtain_auth_token),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('rest-auth',include('rest_auth.urls')),
    path('admin/', admin.site.urls),
    path('rest-auth/registration/',include("rest_auth.registration.urls"))
]
urlpatterns +=static(
        prefix=settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
        )
