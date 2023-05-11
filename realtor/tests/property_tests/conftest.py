import pytest
from properties.models import Property


@pytest.fixture
def auto_info_present():
    return {
        "price": 50,
        "city": "서울시",
        "district": "강서구",
        "zone": "마곡동",
        "size": 83,
        "description": "nothing",
        "maintenance_cost": 16,
    }


@pytest.fixture
def create_property(db, Property, auto_info_present):
    def make_property(**kwargs):
        kwargs["price"] = auto_info_present["price"]
        kwargs["city"] = auto_info_present["city"]
        kwargs["district"] = auto_info_present["district"]
        kwargs["zone"] = auto_info_present["zone"]
        kwargs["size"] = auto_info_present["size"]
        kwargs["description"] = auto_info_present["description"]
        kwargs["maintenance_cost"] = auto_info_present["maintenance_cost"]

        return Property.objects.create(**kwargs)

    return make_property
