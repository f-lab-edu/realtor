from django.urls import include, path
from rest_framework import routers

from .views import UserViewSet
from .views import AgentViewSet

from ..transactions.urls import applicationRouter, contractRouter
from ..properties.urls import preferredRouter

userRouter = routers.DefaultRouter()
userRouter.register("users", UserViewSet, basename = "user")

agentRouter = routers.DefaultRouter()
agentRouter.register("agents", AgentViewSet, basename = "agent")

urlpatterns = [
    path("", include(userRouter.urls)),
    path("", include(agentRouter.urls)),
    path("users/application/", include(applicationRouter.urls)),
    path("users/preferredProperties", include(preferredRouter.urls)),
    path("agents/contracts", include(contractRouter.urls)),
]