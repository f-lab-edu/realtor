from rest_framework import generics
from transactions.serializers import AgentSerializer, ContractSerializer

from .models import Agent, Contract


class AgentList(generics.ListCreateAPIView):

    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

    def get(self, request, *args, **kwargs):  # admin monitors all users
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AgentDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Agent.objects.all()
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
        return Contract.objects.filter(agent=self.kwargs["pk"])

    def get(self, request, *args, **kwargs):  # admin monitors all users
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ContractDetail(generics.RetrieveUpdateDestroyAPIView):

    lookup_field = "id"

    def get_queryset(self):
        return Contract.objects.filter(agent=self.kwargs["pk"])

    serializer_class = ContractSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
