from properties.models import City, District, Property, Zone
from properties.serializers import CitySerializer, DistrictSerializer, PropertySerializer, ZoneSerializer
from rest_framework import generics, serializers


class PropertyList(generics.ListCreateAPIView):
    def get_queryset(self):
        return Property.objects.filter(city=self.kwargs["pk"], district=self.kwargs["d_id"])

    serializer_class = PropertySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PropertyDetail(generics.RetrieveUpdateDestroyAPIView):

    lookup_field = "p_id"

    def get_queryset(self):
        return Property.objects.filter(city=self.kwargs["pk"], district=self.kwargs["d_id"])

    serializer_class = PropertySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CityList(generics.ListCreateAPIView):

    queryset = City.objects.all()
    serializer_class = CitySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CityDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = City.objects.all()
    serializer_class = CitySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class DistrictList(generics.ListCreateAPIView):
    def get_queryset(self):

        return District.objects.filter(city=self.kwargs["pk"])

    serializer_class = DistrictSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class DistrictDetail(generics.RetrieveUpdateDestroyAPIView):

    lookup_field = "d_id"

    def get_queryset(self):

        return District.objects.filter(city=self.kwargs["pk"])

    serializer_class = DistrictSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ZoneList(generics.ListCreateAPIView):
    def get_queryset(self):

        return Zone.objects.filter(district=self.kwargs["d_id"])

    serializer_class = ZoneSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ZoneDetail(generics.RetrieveUpdateDestroyAPIView):

    lookup_field = "z_id"

    def get_queryset(self):

        return Zone.objects.filter(district=self.kwargs["d_id"])

    serializer_class = ZoneSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
