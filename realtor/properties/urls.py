from django.urls import include, path
from rest_framework import routers

from .views import PropertyViewSet, PreferredPropertyViewSet


router = routers.DefaultRouter()
router.register("properties", PropertyViewSet, basename="property");

preferredRouter = routers.DefaultRouter()
router.register("preferredProperty", PreferredPropertyViewSet, basename = "preferredProperty")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(preferredRouter.urls))
]