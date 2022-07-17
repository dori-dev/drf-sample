from django.urls import path
from rest_framework.routers import SimpleRouter
from planes.views import PlaneView, PlaneItemView, PlaneViewSet

router = SimpleRouter()
router.register('planes', PlaneViewSet)

urlpatterns = [
    path('plane/', PlaneView.as_view()),
    path('plane/<int:pk>/', PlaneItemView.as_view()),
] + router.urls
