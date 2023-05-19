import uuid

import pytest


@pytest.fixture
def create_user(db, django_user_model):
    def make_user(**kwargs):
        auth_info_preset = {
            "password": "strong-test-pass",
            "phone": "01000000000",
            "date_joined": "2023-05-08T22:55:10.837518Z",
        }
        kwargs |= auth_info_preset

        if "username" not in kwargs:
            kwargs["username"] = str(uuid.uuid4())
        return django_user_model.objects.create_user(**kwargs)

    return make_user
