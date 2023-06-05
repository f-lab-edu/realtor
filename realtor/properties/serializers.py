from rest_framework import serializers

from .models import City, District, Property, Zone


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"


class DistrictSerializer(serializers.ModelSerializer):
    city = CitySerializer(many=False, read_only=True)

    class Meta:
        model = District
        fields = "__all__"


class ZoneSerializer(serializers.ModelSerializer):
    district = DistrictSerializer(many=False, read_only=True)

    class Meta:
        model = Zone
        fields = "__all__"


class PropertySerializer(serializers.ModelSerializer):
    district = DistrictSerializer(many=False, read_only=True)
    city = CitySerializer(many=False, read_only=True)
    zone = ZoneSerializer(many=False, read_only=True)

    class Meta:
        model = Property
        fields = [
            "id",
            "image",
            "price",
            "city",
            "district",
            "zone",
            "property_type",
            "detailed_type",
            "size",
            "description",
            "maintenance_cost",
            "status",
        ]
