"""otp admin
"""
from django.contrib import admin

from otp.models import User, Profile, OtpRequest


class OtpRequestAdmin(admin.ModelAdmin):
    """Otp requests admin model
    """
    list_display = ['phone', 'channel', 'password']
    list_filter = ['phone', 'channel']


class ProfileAdmin(admin.ModelAdmin):
    """User profile admin model
    """
    list_display = ['user', 'birth_date']


admin.site.register(User)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(OtpRequest, OtpRequestAdmin)
