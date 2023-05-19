from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from users import views

urlpatterns = [
    path("", views.UserList.as_view()),
    path("<int:pk>/", views.UserDetail.as_view()),
    path("<int:pk>/applications/", views.ApplicationList.as_view()),
    path("<int:pk>/applications/<int:id>/", views.ApplicationDetail.as_view()),
    path("<int:pk>/preferredProperties/", views.PreferredPropertyList.as_view()),
    path("<int:pk>/preferredProperties/<int:id>/", views.PreferredPropertyDetail.as_view()),
    path("<int:pk>/agents/", views.AgentList.as_view()),
    path("<int:pk>/agents/<int:id>/", views.AgentDetail.as_view()),
    path("<int:pk>/agents/<int:aid>/contracts/", views.ContractList.as_view()),
    path("<int:pk>/agents/<int:aid>/contracts/<int:id>/", views.ContractDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
