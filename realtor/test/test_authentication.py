import pytest
from users.models import User


def test_an_admin_view(admin_client):
    response = admin_client.get("/admin/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_registration_api(client):

    data = {
        "username": "salr",
        "first_name": "sang",
        "last_name": "joe",
        "email": "salr921@naver.com",
        "password": "wjddk12wjddk",
    }

    response = client.post("http://localhost:8000/authentication/registration/", json=data)
    assert response.status_code == 200
