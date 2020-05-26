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
def authenticated_user():
    return get_model_fixture(User)


@pytest.mark.django_db
def test_subscription_plan_list_unauthenticated_user_forbidden(api_client):
    api_client.force_authenticate(user=AnonymousUser())
    url = reverse('api:v1:subscriptions-list')
    response = api_client.get(url, params={'enterprise_uuid': 'foo'})
    assert status.HTTP_403_FORBIDDEN == response.status_code


@pytest.mark.django_db
def test_subscription_plan_retrieve_unauthenticated_user_forbidden(api_client):
    api_client.force_authenticate(user=AnonymousUser())
    url = reverse('api:v1:subscriptions-detail', kwargs={'subscription_uuid': 'foo'})
    response = api_client.get(url)
    assert status.HTTP_403_FORBIDDEN == response.status_code


@pytest.mark.django_db
def test_license_list_unauthenticated_user_forbidden(api_client):
    api_client.force_authenticate(user=AnonymousUser())
    url = reverse('api:v1:licenses-list', kwargs={'subscription_uuid': 'foo'})
    response = api_client.get(url)
    assert status.HTTP_403_FORBIDDEN == response.status_code


@pytest.mark.django_db
def test_license_retrieve_unauthenticated_user_forbidden(api_client):
    api_client.force_authenticate(user=AnonymousUser())
    url = reverse('api:v1:licenses-detail', kwargs={'subscription_uuid': 'foo', 'license_uuid': 'bar'})
    response = api_client.get(url)
    assert status.HTTP_403_FORBIDDEN == response.status_code
