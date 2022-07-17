"""Plane urls
/planes/
/planes/{id}
"""
from rest_framework.routers import SimpleRouter
from planes.views import PlaneViewSet

router = SimpleRouter()
router.register('planes', PlaneViewSet)

urlpatterns = router.urls
