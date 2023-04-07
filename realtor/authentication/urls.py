from authentication import views
from django.urls import path

urlpatterns = [
    path("", views.RegistrationView.as_view()),
]
