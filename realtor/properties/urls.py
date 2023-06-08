from django.urls import path
from properties import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("", views.CityList.as_view()),
    path("<int:pk>/", views.CityDetail.as_view()),
    path("<int:pk>/districts/", views.DistrictList.as_view()),
    path("<int:pk>/districts/<int:d_id>/", views.DistrictDetail.as_view()),
    path("<int:pk>/districts/<int:d_id>/properteis/", views.PropertyList.as_view()),
    path("<int:pk>/districts/<int:d_id>/properteis/<int:p_id>/", views.PropertyDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
