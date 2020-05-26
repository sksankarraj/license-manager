"""
Tests for the Subscription and License V1 API view sets.
"""
import pytest
from django.contrib.auth.models import AnonymousUser
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from django_dynamic_fixture import get as get_model_fixture

from license_manager.apps.core.models import User


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def unauthenticated_user():
    return AnonymousUser()


@pytest.fixture
def authenticated_user():
    return get_model_fixture(User)


@pytest.mark.django_db
def test_subscription_plan_list_unauthenticated_user_forbidden(api_client, unauthenticated_user):
    api_client.force_authenticate(user=unauthenticated_user)
    url = reverse('api:v1:subscriptions-list', kwargs={'enterprise_uuid': '1234'})
    response = api_client.get(url)
    assert status.HTTP_403_FORBIDDEN == response.status_code
