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
    """
    Fixture that provides a DRF test APIClient.
    """
    return APIClient()


@pytest.fixture
def non_staff_user():
    """
    Fixture that provides a plain 'ole authenticated User instance.
    Non-staff, non-admin.
    """
    return get_model_fixture(User)


@pytest.fixture
def staff_user():
    """
    Fixture that provides a User instance for whom staff=True.
    """
    return get_model_fixture(User, is_staff=True, is_superuser=False)


@pytest.fixture
def super_user():
    """
    Fixture that provides a superuser.
    """
    return get_model_fixture(User, is_staff=True, is_superuser=True)


def _subscriptions_list_request(api_client, user, enterprise_uuid=None):
    """
    Helper method that requests a list of subscriptions entities for a given enterprise_uuid.
    """
    api_client.force_authenticate(user=user)
    url = reverse('api:v1:subscriptions-list')
    params = {}
    if enterprise_uuid is not None:
        params['enterprise_uuid'] = enterprise_uuid
    return api_client.get(url, params=params)


def _subscriptions_detail_request(api_client, user, subscription_uuid):
    """
    Helper method that requests details for a specific subscription_uuid.
    """
    api_client.force_authenticate(user=user)
    url = reverse('api:v1:subscriptions-detail', kwargs={'subscription_uuid': subscription_uuid})
    return api_client.get(url)


def _licenses_list_request(api_client, user, subscription_uuid):
    """
    Helper method that requests a list of licenses for a given subscription_uuid.
    """
    api_client.force_authenticate(user=user)
    url = reverse('api:v1:licenses-list', kwargs={'subscription_uuid': subscription_uuid})
    return api_client.get(url)


def _licenses_detail_request(api_client, user, subscription_uuid, license_uuid):
    """
    Helper method that requests details for a specific license_uuid.
    """
    api_client.force_authenticate(user=user)
    url = reverse('api:v1:licenses-detail', kwargs={
        'subscription_uuid': subscription_uuid,
        'license_uuid': license_uuid
    })
    return api_client.get(url)


def test_subscription_plan_list_unauthenticated_user_403(api_client):
    response = _subscriptions_list_request(api_client, AnonymousUser(), enterprise_uuid='foo')
    assert status.HTTP_403_FORBIDDEN == response.status_code


def test_subscription_plan_retrieve_unauthenticated_user_403(api_client):
    response = _subscriptions_detail_request(api_client, AnonymousUser(), subscription_uuid='bar')
    assert status.HTTP_403_FORBIDDEN == response.status_code


def test_license_list_unauthenticated_user_403(api_client):
    response = _licenses_list_request(api_client, AnonymousUser(), subscription_uuid='foo')
    assert status.HTTP_403_FORBIDDEN == response.status_code


def test_license_retrieve_unauthenticated_user_403(api_client):
    response = _licenses_detail_request(api_client, AnonymousUser(), 'foo', 'bar')
    assert status.HTTP_403_FORBIDDEN == response.status_code


def test_subscription_plan_list_non_staff_user_403(api_client, non_staff_user):
    response = _subscriptions_list_request(api_client, non_staff_user, enterprise_uuid='foo')
    assert status.HTTP_403_FORBIDDEN == response.status_code


def test_subscription_plan_detail_non_staff_user_403(api_client, non_staff_user):
    response = _subscriptions_detail_request(api_client, non_staff_user, subscription_uuid='bar')
    assert status.HTTP_403_FORBIDDEN == response.status_code


def test_licenses_list_non_staff_user_403(api_client, non_staff_user):
    response = _licenses_list_request(api_client, non_staff_user, subscription_uuid='foo')
    assert status.HTTP_403_FORBIDDEN == response.status_code


def test_license_detail_non_staff_user_403(api_client, non_staff_user):
    response = _licenses_detail_request(api_client, non_staff_user, subscription_uuid='bar', license_uuid='bar')
    assert status.HTTP_403_FORBIDDEN == response.status_code


# Tests below all require accessing the database, so we use a Django TestCase,
# instead of pytest-style test functions.
@pytest.mark.django_db
def test_subscription_plan_list_staff_user_200(api_client, staff_user):
    # TODO: make sure there are subscriptions to return data about in the test response
    response = _subscriptions_list_request(api_client, staff_user, enterprise_uuid='foo')
    assert status.HTTP_200_OK == response.status_code
    # TODO: assert something about the shape and size of the data


@pytest.mark.django_db
def test_subscription_plan_details_staff_user_200(api_client, staff_user):
    # TODO: make sure there are subscriptions to return data about in the test response
    response = _subscriptions_detail_request(api_client, staff_user, subscription_uuid='bar')
    assert status.HTTP_200_OK == response.status_code
    # TODO: assert something about the shape and size of the data


@pytest.mark.django_db
def test_license_list_staff_user_200(api_client, staff_user):
    # TODO: make sure there are licenses to return data about in the test response
    response = _licenses_list_request(api_client, staff_user, subscription_uuid='foo')
    assert status.HTTP_200_OK == response.status_code
    # TODO: assert something about the shape and size of the data


@pytest.mark.django_db
def test_license_detail_staff_user_200(api_client, staff_user):
    # TODO: make sure there are subscriptions to return data about in the test response
    response = _licenses_detail_request(api_client, staff_user, subscription_uuid='foo', license_uuid='bar')
    assert status.HTTP_200_OK == response.status_code
    # TODO: assert something about the shape and size of the data


@pytest.mark.django_db
def test_subscription_plan_list_super_user_200(api_client, super_user):
    pass


@pytest.mark.django_db
def test_subscription_plan_details_super_user_200(api_client, super_user):
    pass


@pytest.mark.django_db
def test_license_list_super_user_200(api_client, super_user):
    pass


@pytest.mark.django_db
def test_license_detail_super_user_200(api_client, super_user):
    pass
