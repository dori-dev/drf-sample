"""Plane views
"""
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters, authentication, permissions
from django_filters.rest_framework import DjangoFilterBackend
from planes.models import Plane
from planes.serializers import PlaneSerializer


class PlaneViewSet(ModelViewSet):
    """
    Plane Api, get, create, delete, update planes
        get, post: /api/planes/
        get, delete, put, patch: /api/planes/id/
    """
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
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (
        authentication.TokenAuthentication,
    )
