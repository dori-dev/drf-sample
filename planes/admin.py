"""Plane admin
"""
from django.contrib import admin
from planes.models import Plane


class PlaneAdmin(admin.ModelAdmin):
    list_display = ('plane_from', 'plane_to', 'plane_time',
                    'arrive_time', 'capacity')


admin.site.register(Plane, PlaneAdmin)
