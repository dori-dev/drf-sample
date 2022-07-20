"""config URL Configuration
"""
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('planes.urls')),
    path('token/', obtain_auth_token),
]
