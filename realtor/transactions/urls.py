from django.urls import include, path
from rest_framework import routers

from .views import ContractViewSet
from .views import ApplicationViewSet


router = routers.DefaultRouter()
router.register("applications", ApplicationViewSet, basename = "application")


urlpatterns = [
    path(),
]