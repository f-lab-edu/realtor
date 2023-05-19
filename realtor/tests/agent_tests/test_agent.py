import json

import pytest
from users.models import Agent, User


@pytest.mark.django_db
def test_agent(client):
    user = User.objects.create(username="sanghun")
    user_id = user.id

    response = client.get(f"/users/{user_id}/agents/")
    assert response.status_code == 200

    payload = {"rating": 0.3}

    response = client.post(
        f"/users/{user_id}/agents/", data=json.dumps(dict(payload)), content_type="application/json"
    )
    assert response.status_code == 201

    id = response.json()["id"]

    response = client.get(f"/users/{user_id}/agents/")
    assert response.status_code == 200
    assert Agent.objects.count() == 1

    payload = {"rating": 0.1}

    response = client.put(
        f"/users/{user_id}/agents/{id}", data=json.dumps(dict(payload)), content_type="application/json"
    )
    assert response.status_code == 301
