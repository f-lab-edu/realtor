from django.urls import include, path
from rest_framework import routers

from .views import UserViewSet
from .views import AgentViewSet


router = routers.DefaultRouter()
router.register("users", UserViewSet, basename = "user")


urlpatterns = [
    path("", include(router.urls)),
]