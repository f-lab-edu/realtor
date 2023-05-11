import json

import pytest
from properties.models import Property
from users.models import User


@pytest.mark.django_db
def test_property(client):
    user = User.objects.create(username="sang")
    user_id = user.id

    response = client.get("/properties/")
    assert response.status_code == 200
    assert Property.objects.count() == 0

    payload = {
        "price": 50,
        "city": "서울시",
        "district": "강서구",
        "zone": "마곡동",
        "size": 83,
        "description": "nothing",
        "maintenance_cost": 16,
        "user_id": 3,
    }
    response = client.post("/properties/", data=json.dumps(dict(payload)), content_type="application/json")
    assert response.status_code == 201
    assert Property.objects.count() == 1

    id = response.json()["id"]

    response = client.get(f"/properties/{id}/")
    assert response.status_code == 200
    assert Property.objects.values()[0] == {
        "id": 1,
        "image": "",
        "price": 50,
        "city": "서울시",
        "district": "강서구",
        "zone": "마곡동",
        "property_type": 1,
        "detailed_type": 4,
        "size": 83,
        "description": "nothing",
        "maintenance_cost": 16,
        "status": 1,
        "user_id": None,
    }

    payload = {"status": 1}

    response = client.patch(f"/properties/{id}/", data=json.dumps(dict(payload)), content_type="application/json")
    assert response.status_code == 200

    response = client.delete(f"/properties/{id}/")
    assert response.status_code == 204

    response = client.patch(f"/properties/{id}/", data=json.dumps(dict(payload)), content_type="application/json")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not found."}
