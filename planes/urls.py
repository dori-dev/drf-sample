from django.urls import path
from planes.views import PlaneAPIView, PlaneItemView

urlpatterns = [
    path('planes/', PlaneAPIView.as_view()),
    path('planes/<int:pk>/', PlaneItemView.as_view()),
]
