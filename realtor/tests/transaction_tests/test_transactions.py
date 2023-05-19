import json

import pytest
from transactions.models import Agent, Contract


@pytest.mark.django_db
def test_transaction(client):
    agent = Agent.objects.create(rating=4.3)

    assert agent.id == 1
