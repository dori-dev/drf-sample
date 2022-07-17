# from rest_framework.generics import (
#     RetrieveUpdateDestroyAPIView, ListCreateAPIView)
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from planes.models import Plane
from planes.serializers import PlaneSerializer


# class PlaneView(ListCreateAPIView):
#     queryset = Plane.objects.all()
#     serializer_class = PlaneSerializer


# class PlaneItemView(RetrieveUpdateDestroyAPIView):
#     queryset = Plane.objects.all()
#     serializer_class = PlaneSerializer


class PlaneViewSet(ModelViewSet):
    queryset = Plane.objects.all()
    serializer_class = PlaneSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend
    ]
    filterset_fields = ['plane_from', 'plane_to']
    search_fields = ['plane_from', 'plane_to']
    ordering_fields = [
        'id', 'capacity',
        'plane_time', 'arrive_time'
    ]
