from django.urls import include, path
from rest_framework import routers

from .views import PropertyViewSet


router = routers.DefaultRouter()
router.register("properties", PropertyViewSet, basename="property");


urlpatterns = [
    path("", include(router.urls)),
]