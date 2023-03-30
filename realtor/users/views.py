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

    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ApplicationDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PreferredPropertyList(generics.ListCreateAPIView):

    queryset = PreferredProperty.objects.all()
    serializer_class = PreferredPropertySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PreferredPropertyDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = PreferredProperty.objects.all()
    serializer_class = PreferredPropertySerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
