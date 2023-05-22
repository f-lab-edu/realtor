from django.shortcuts import get_object_or_404
from rest_framework import generics
from users.models import Agent, Application, Contract, PreferredProperty, User
from users.serializers import (
    AgentSerializer,
    ApplicationSerializer,
    ContractSerializer,
    PreferredPropertySerializer,
    UserSerializer,
)


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
    def get_queryset(self):

        return Application.objects.filter(user=self.kwargs["pk"])

    serializer_class = ApplicationSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def perform_create(self, serializer):
        foreign_key_id = self.kwargs["pk"]
        user = User.objects.get(id=foreign_key_id)
        serializer.save(user=user)


class ApplicationDetail(generics.RetrieveUpdateDestroyAPIView):

    lookup_field = "id"

    def get_queryset(self):

        return Application.objects.filter(user=self.kwargs["pk"])

    serializer_class = ApplicationSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PreferredPropertyList(generics.ListCreateAPIView):
    def get_queryset(self):

        return PreferredProperty.objects.filter(users=self.kwargs["pk"])

    serializer_class = PreferredPropertySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def perform_create(self, serializer):
        foreign_key_id = self.kwargs["pk"]
        user = User.objects.get(id=foreign_key_id)
        serializer.save(user=user)


class PreferredPropertyDetail(generics.RetrieveUpdateDestroyAPIView):

    lookup_field = "id"

    def get_queryset(self):
        return PreferredProperty.objects.filter(users=self.kwargs["pk"])

    serializer_class = PreferredPropertySerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class AgentList(generics.ListCreateAPIView):

    serializer_class = AgentSerializer

    def get_queryset(self):
        return Agent.objects.filter(user=self.kwargs["pk"])

    def get(self, request, *args, **kwargs):  # admin monitors all users
        return self.list(request, *args, **kwargs)

    def perform_create(self, serializer):
        agent_id = self.kwargs["pk"]
        user = User.objects.get(id=agent_id)
        serializer.save(user=user)


class AgentDetail(generics.RetrieveUpdateDestroyAPIView):

    lookup_field = "id"

    def get_queryset(self):
        return Agent.objects.filter(user=self.kwargs["pk"])

    serializer_class = AgentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ContractList(generics.ListCreateAPIView):

    serializer_class = ContractSerializer

    def get_queryset(self):
        return Contract.objects.filter(user=self.kwargs["pk"], agent=self.kwargs["aid"])

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def perform_create(self, serializer):
        user_id = self.kwargs["pk"]
        user = User.objects.get(id=user_id)
        agent_id = self.kwargs["aid"]
        agent = Agent.objects.get(id=agent_id)
        serializer.save(user=user, agent=agent)


class ContractDetail(generics.RetrieveUpdateDestroyAPIView):

    lookup_field = "id"

    def get_queryset(self):
        return Contract.objects.filter(user=self.kwargs["pk"], agent=self.kwargs["aid"])

    serializer_class = ContractSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
