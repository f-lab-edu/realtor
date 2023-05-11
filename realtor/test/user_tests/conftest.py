import uuid

import pytest


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
