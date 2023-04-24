from django.shortcuts import get_object_or_404
from rest_framework import generics
from users.models import Application, PreferredProperty, User
from users.serializers import ApplicationSerializer, PreferredPropertySerializer, UserSerializer


class UserList(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):  # admin monitors all users
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ApplicationList(generics.ListCreateAPIView):
    model = Application

    def get_queryset(self):
        return self.model.objects.filter(user=self.kwargs["pk"])

    serializer_class = ApplicationSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ApplicationDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Application
    lookup_field = "id"

    def get_queryset(self):
        print(self.kwargs)
        return self.model.objects.filter(user=self.kwargs["pk"])

    serializer_class = ApplicationSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PreferredPropertyList(generics.ListCreateAPIView):

    model = PreferredProperty

    def get_queryset(self):
        return self.model.objects.filter(users=self.kwargs["pk"])

    serializer_class = PreferredPropertySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PreferredPropertyDetail(generics.RetrieveUpdateDestroyAPIView):

    model = PreferredProperty
    lookup_field = "id"

    def get_queryset(self):
        return self.model.objects.filter(users=self.kwargs["pk"])

    serializer_class = PreferredPropertySerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
