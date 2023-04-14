from authentication import views
from django.urls import path

urlpatterns = [
    path("registration/", views.RegistrationView.as_view()),
    path("login/", views.LoginView.as_view()),
]
