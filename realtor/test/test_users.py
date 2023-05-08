import json
import uuid

import pytest
from users.models import User
from users.serializers import UserSerializer


@pytest.fixture
def test_password():
    return "strong-test-pass"


@pytest.fixture
def test_phone():
    return "01000000000"


@pytest.fixture
def create_user(db, django_user_model, test_password, test_phone):
    def make_user(**kwargs):
        kwargs["password"] = test_password
        kwargs["phone"] = test_phone
        if "username" not in kwargs:
            kwargs["username"] = str(uuid.uuid4())
        return django_user_model.objects.create_user(**kwargs)

    return make_user


@pytest.mark.django_db
def test_user_create(create_user):
    user = create_user(username="test")
    assert User.objects.count() == 1
    assert user.username == "test"
    assert user.phone == "01000000000"


@pytest.mark.django_db
def test_user_get(client):
    response = client.get("http://localhost:8000/users/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_post(client):
    data = {"username": "dd", "password": "wjddk12edaf", "phone": "01000000900"}
    response = client.post(
        "http://localhost:8000/users/", data=json.dumps(dict(data)), content_type="application/json"
    )

    assert response.status_code == 201


@pytest.mark.django_db
def test_user_delete(client, create_user):

    user = create_user(username="sanghun")
    id = user.id
    response = client.delete(f"http://localhost:8000/users/{id}")
    assert response.json == {}
    assert response.status_code == 200


def test_user_serializer():

    serializer = UserSerializer()
    f = serializer.fields["username"]
    obj = User()

    assert f.to_representation(obj) == ""
    obj.username = "sanghun"
    assert f.to_representation(obj) == "sanghun"
