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
def test_date():
    return "2023-05-08T22:55:10.837518Z"


@pytest.fixture
def create_user(db, django_user_model, test_password, test_phone, test_date):
    def make_user(**kwargs):
        kwargs["password"] = test_password
        kwargs["phone"] = test_phone
        kwargs["date_joined"] = test_date
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
    assert response.json() == []


@pytest.mark.django_db
def test_user_getById(client, create_user):
    user = create_user(username="sang")
    id = user.id
    response = client.get(f"http://localhost:8000/users/{id}/")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "username": "sang",
        "email": "",
        "phone": "01000000000",
        "date_joined": "2023-05-08T22:55:10.837518Z",
    }


@pytest.mark.django_db
def test_user_post(client):
    payload = {
        "username": "dd",
        "password": "wjddk12edaf",
        "phone": "01000000900",
        "date_joined": "2023-05-08T22:55:10.837518Z",
    }
    response = client.post(
        "http://localhost:8000/users/", data=json.dumps(dict(payload)), content_type="application/json"
    )

    assert response.status_code == 201
    assert response.json() == {
        "id": 1,
        "username": "dd",
        "email": "",
        "phone": "01000000900",
        "date_joined": "2023-05-08T22:55:10.837518Z",
    }


@pytest.mark.django_db
def test_user_update(client, create_user):
    payload = {"username": "ded", "phone": "01000000000"}

    user = create_user(username="sang")
    id = user.id
    response = client.put(
        f"http://localhost:8000/users/{id}/", data=json.dumps(dict(payload)), content_type="application/json"
    )
    print(response)
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_delete(client, create_user):

    user = create_user(username="sanghun")
    id = user.id
    response = client.delete(f"http://localhost:8000/users/{id}/")
    assert response.status_code == 204


@pytest.mark.django_db
def test_get_user_not_found(client):
    id = 111111  # dummy id
    response = client.get(f"http://localhost:8000/users/{id}/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not found."}


@pytest.mark.django_db
def test_user_delete_not_found(client):
    id = 111111  # dummy id
    response = client.delete(f"http://localhost:8000/users/{id}/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not found."}


@pytest.mark.django_db
def test_user_update_not_found(client):
    id = 111111  # dummy id
    response = client.put(f"http://localhost:8000/users/{id}/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not found."}


@pytest.mark.django_db
def test_user_post_invalid_field(client):
    payload = {
        "user": "dd",
    }
    response = client.post(
        "http://localhost:8000/users/", data=json.dumps(dict(payload)), content_type="application/json"
    )
    assert response.status_code == 400
    assert response.json() == {"username": ["This field is required."], "phone": ["This field is required."]}


def test_user_serializer():

    serializer = UserSerializer()
    f = serializer.fields["username"]
    obj = User()

    assert f.to_representation(obj) == ""
    obj.username = "sanghun"
    assert f.to_representation(obj) == "sanghun"
