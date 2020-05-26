from collections import OrderedDict

from django.shortcuts import get_object_or_404
from edx_rest_framework_extensions.auth.jwt.authentication import (
    JwtAuthentication,
)
from rest_framework import permissions, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView


class BaseViewSet(viewsets.GenericViewSet):
    """
    Base class for all license manager view sets.
    """
    authentication_classes = [JwtAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class SubscriptionViewSet(ListModelMixin, BaseViewSet):
    """ Viewset for CRUD operations on Subscriptions."""
    renderer_classes = [JSONRenderer]
    lookup_field = 'enterprise_uuid'

    def get_queryset(self):
        raise NotImplementedError

    def list(self, request, enterprise_uuid):
        raise NotImplementedError


class LicenseViewSet(ListModelMixin, BaseViewSet):
    """ Viewset for CRUD operations on Licenses."""
    renderer_classes = [JSONRenderer]
    lookup_field = 'subscription_uuid'

    def get_queryset(self):
        raise NotImplementedError
