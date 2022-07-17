from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView)
from rest_framework.viewsets import ModelViewSet
from planes.models import Plane
from planes.serializers import PlaneSerializer


class PlaneView(ListCreateAPIView):
    queryset = Plane.objects.all()
    serializer_class = PlaneSerializer


class PlaneItemView(RetrieveUpdateDestroyAPIView):
    queryset = Plane.objects.all()
    serializer_class = PlaneSerializer


class PlaneViewSet(ModelViewSet):
    queryset = Plane.objects.all()
    serializer_class = PlaneSerializer
