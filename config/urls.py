"""config URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="DRF Sample - Docs",
        default_version='v2',
        description="Hello, I'm Mohammad Dori and this is"
        "sample project for django rest framework.",
        terms_of_service="https://github.com/dori-dev/drf-sample",
        contact=openapi.Contact(email="mr.dori.dev@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('planes.urls')),
    path('otp/', include('otp.urls')),
    path('token/', obtain_auth_token),
    path('', schema_view.with_ui(
        'swagger',
        cache_timeout=0),
        name='schema-swagger-ui'
    ),
]
