from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView)
from planes.models import Plane
from planes.serializers import PlaneSerializer


class PlaneAPIView(ListCreateAPIView):
    queryset = Plane.objects.all()
    serializer_class = PlaneSerializer


class PlaneItemView(RetrieveUpdateDestroyAPIView):
    queryset = Plane.objects.all()
    serializer_class = PlaneSerializer
