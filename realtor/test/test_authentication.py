import json
import uuid

import pytest
from users.models import User


@pytest.fixture
def register_user(db, django_user_model):
    def make_user(**kwargs):
        kwargs["first_name"] = "sang"
        kwargs["last_name"] = "joe"
        kwargs["email"] = "salr921@naver.com"
        kwargs["password"] = "wjddk12wjddk"
        kwargs["is_staff"] = True
        if "username" not in kwargs:
            kwargs["username"] = str(uuid.uuid4())
        return django_user_model.objects.create_user(**kwargs)

    return make_user


@pytest.fixture
def auto_login_user(db, client, register_user):
    def make_auto_login(user=None):
        if user is None:
            user = register_user()
        client.login(username=user.username, password="wjddk12wjddk")
        return client, user

    return make_auto_login


def test_unauthorized(client):
    response = client.get("/admin/")
    assert response.status_code == 302  # when unauthorized user access to the admin page, it redirects to a login page


def test_authorized(admin_client):
    response = admin_client.get("/admin/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_auth_login(auto_login_user):
    client, user = auto_login_user()
    response = client.get("/admin/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_registration_superuser_api(client):

    data = {
        "username": "salr",
        "first_name": "sang",
        "last_name": "joe",
        "email": "salr921@naver.com",
        "password": "wjddk12wjddk",
    }

    response = client.post(
        "/authentication/registration/",
        data=json.dumps(dict(data)),
        content_type="application/json",
    )
    assert response.status_code == 200
    assert "token" in response.json()


@pytest.mark.django_db
def test_registration_duplicated_username_api(client, register_user):

    register_user(username="salr")
    payload = {
        "username": "salr",
        "first_name": "sang",
        "last_name": "joe",
        "email": "salr921@naver.com",
        "password": "wjddk12wjddk",
    }

    response = client.post(
        "/authentication/registration/",
        data=json.dumps(dict(payload)),
        content_type="application/json",
    )
    assert response.status_code == 200
    assert response.json() == {"username": ["A user with that username already exists."]}


@pytest.mark.django_db
def test_registration_short_username_api(client):

    data = {
        "username": "e",
        "first_name": "sang",
        "last_name": "joe",
        "email": "salr921@naver.com",
        "password": "wjddk12wjddk",
    }

    response = client.post(
        "/authentication/registration/",
        data=json.dumps(dict(data)),
        content_type="application/json",
    )
    assert response.status_code == 200
    assert response.json() == {"username": ["username is too short!"]}


@pytest.mark.django_db
def test_login_api(client, register_user):
    register_user(username="sang")
    payload = {
        "username": "sang",
        "password": "wjddk12wjddk",
    }
    response = client.post("/authentication/login/", data=json.dumps(dict(payload)), content_type="application/json")
    assert response.status_code == 200
    assert "sang" == response.json()["username"]


@pytest.mark.django_db
def test_login_not_matched_payload_api(client, register_user):
    register_user(username="sang")
    payload = {
        "username": "sang",
        "password": "d",
    }
    response = client.post("/authentication/login/", data=json.dumps(dict(payload)), content_type="application/json")
    assert response.status_code == 400
    assert response.json() == {"non_field_errors": ["A user with this username and password was not found"]}


@pytest.mark.django_db
def test_login_invalid_payload_api(client, register_user):
    register_user(username="sang")
    payload = {}
    response = client.post("/authentication/login/", data=json.dumps(dict(payload)), content_type="application/json")
    assert response.status_code == 400
    assert response.json() == {"username": ["This field is required."], "password": ["This field is required."]}


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()


@pytest.mark.django_db
@pytest.mark.parametrize(
    "username, password, status_code",
    [
        (None, None, 400),
        (None, "wjddk12wjddk", 400),
        ("sanghun", None, 400),
        ("sanghun", "wjddk12wjddk", 200),
    ],
)
def test_login_parametrizing_api(api_client, username, password, status_code, register_user):
    register_user(username="sanghun")
    payload = {
        "username": username,
        "password": password,
    }
    response = api_client.post(
        "/authentication/login/", data=json.dumps(dict(payload)), content_type="application/json"
    )
    print(response.json())
    assert response.status_code == status_code
