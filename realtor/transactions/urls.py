from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("", views.AgentList.as_view()),
    path("<int:pk>/", views.AgentDetail.as_view()),
    path("<int:pk>/contracts/", views.ContractList.as_view()),
    # path("<int:pk>/contracts/<int:pk>", views.ContractDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
