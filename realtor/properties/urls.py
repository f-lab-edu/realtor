from django.urls import include, path
from properties import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("", views.PropertyList.as_view()),
    path("<int:pk>/", views.PropertyDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
