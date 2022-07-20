"""otp urls
"""
from django.urls import path
from otp.views import RequestOtpAPI, VerifyOtpAPI

urlpatterns = [
    path('request/', RequestOtpAPI.as_view()),
    path('verify/', VerifyOtpAPI.as_view()),
]
