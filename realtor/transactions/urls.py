from django.urls import include, path
from rest_framework import routers

from .views import ContractViewSet
from .views import ApplicationViewSet


applicationRouter = routers.DefaultRouter()
applicationRouter.register("applications", ApplicationViewSet, basename = "application")

contractRouter = routers.DefaultRouter()
contractRouter.register("contracts", ContractViewSet)

urlpatterns = [
    path("", include(applicationRouter.urls)),
    path("", include(contractRouter.urls))
]