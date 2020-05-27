from collections import OrderedDict

from django.shortcuts import get_object_or_404
from edx_rest_framework_extensions.auth.jwt.authentication import (
    JwtAuthentication,
)
from rest_framework import (
    authentication,
    permissions,
    status,
    viewsets,
)
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class ViewSetBaseAuthMixin:
    """
    Mixin that defines the minimum required
    `authentication_classess` and `permission_classes` fields
    for the ViewSets below.
    """
    authentication_classes = [JwtAuthentication, authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class SubscriptionViewSet(ViewSetBaseAuthMixin, viewsets.ReadOnlyModelViewSet):
    """ Viewset for CRUD operations on Subscriptions."""
    renderer_classes = [JSONRenderer]
    lookup_field = 'uuid'
    lookup_url_kwarg = 'subscription_uuid'

    def get_queryset(self):
        return []

    def list(self, request):
        return Response('', status.HTTP_501_NOT_IMPLEMENTED)

    def retrieve(self, request, subscription_uuid):
        return Response('', status.HTTP_501_NOT_IMPLEMENTED)


class LicenseViewSet(ViewSetBaseAuthMixin, viewsets.ReadOnlyModelViewSet):
    """ Viewset for CRUD operations on Licenses."""
    renderer_classes = [JSONRenderer]
    lookup_field = 'uuid'
    lookup_url_kwarg = 'license_uuid'

    def get_queryset(self):
        return []

    def list(self, request, subscription_uuid):
        return Response('', status.HTTP_501_NOT_IMPLEMENTED)

    def retrieve(self, request, subscription_uuid, license_uuid):
        return Response('', status.HTTP_501_NOT_IMPLEMENTED)
