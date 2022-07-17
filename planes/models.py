from django.db import models


class Plane(models.Model):
    plane_from = models.CharField(
        verbose_name='from',
        max_length=255)
    plane_to = models.CharField(
        verbose_name='to',
        max_length=255)
    plane_time = models.DateTimeField()
    arrive_time = models.DateTimeField()
    capacity = models.SmallIntegerField()
