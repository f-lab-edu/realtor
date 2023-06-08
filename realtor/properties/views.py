from properties.models import City, District, Property, Zone
from properties.serializers import CitySerializer, DistrictSerializer, PropertySerializer, ZoneSerializer
from rest_framework import generics, serializers


class PropertyList(generics.ListCreateAPIView):

    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        if self.request.method == "POST":
            city_id = self.request.data.get("city")
            if city_id:
                context["district_queryset"] = District.objects.filter(city_id=city_id)
        return context


class PropertyDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Property.objects.all()
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

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


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

    def perform_create(self, serializer):
        city_id = self.kwargs["pk"]
        city = City.objects.get(id=city_id)
        district_name = self.request.data.get("name")

        valid_districts = get_valid_districts(city)

        if district_name not in valid_districts:
            raise serializers.ValidationError("Invalid district for the provided city")

        serializer.save(city=city)

        def get_valid_districts(self, city):
            valid_districts = []
            if city.name == "서울":
                valid_districts = ["강남구", "강서구"]
            elif city.name == "부산":
                valid_districts = ["해운대구", "서구"]

            return valid_districts


class DistrictDetail(generics.RetrieveUpdateDestroyAPIView):

    lookup_field = "d_id"

    def get_queryset(self):

        return District.objects.filter(city=self.kwargs["pk"])

    serializer_class = DistrictSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
