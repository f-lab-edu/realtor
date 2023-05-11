import uuid

import pytest


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
