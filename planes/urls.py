# from django.urls import path
from rest_framework.routers import SimpleRouter
# from planes.views import PlaneView, PlaneItemView
from planes.views import PlaneViewSet

router = SimpleRouter()
router.register('planes', PlaneViewSet)

urlpatterns = [
    # path('planes/', PlaneView.as_view()),
    # path('planes/<int:pk>/', PlaneItemView.as_view()),
] + router.urls
