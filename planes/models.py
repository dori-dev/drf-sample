"""Plane models
"""
from django.db import models


class Plane(models.Model):
    """Plane model

    Fields:
        plane_from (CharField): Place of origin
        plane_to (CharField): Place of destination
        plane_time (DateTimeField): Airplane flight time
        arrive_time (DateTimeField): Arrival time of the plane
        capacity (SmallIntegerField): The airplane capacity
    """
    plane_from = models.CharField(
        verbose_name='from',
        max_length=255)
    plane_to = models.CharField(
        verbose_name='to',
        max_length=255)
    plane_time = models.DateTimeField()
    arrive_time = models.DateTimeField()
    capacity = models.SmallIntegerField()
