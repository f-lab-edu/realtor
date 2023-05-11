import uuid

import pytest


@pytest.fixture
def auth_info_preset():
    return {
        "password": "strong-test-pass",
        "phone": "01000000000",
        "date_joined": "2023-05-08T22:55:10.837518Z",
    }


@pytest.fixture
def create_user(db, django_user_model, auth_info_preset):
    def make_user(**kwargs):
        kwargs["password"] = auth_info_preset["password"]
        kwargs["phone"] = auth_info_preset["phone"]
        kwargs["date_joined"] = auth_info_preset["date_joined"]
        if "username" not in kwargs:
            kwargs["username"] = str(uuid.uuid4())
        return django_user_model.objects.create_user(**kwargs)

    return make_user
