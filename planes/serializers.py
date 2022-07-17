"""Plane serializers
"""
from rest_framework import serializers
from planes.models import Plane


class PlaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plane
        fields = (
            'id', 'plane_from', 'plane_to',
            'plane_time', 'arrive_time', 'capacity'
        )
