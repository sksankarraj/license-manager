"""
URL definitions for license manager API version 1.
"""
from django.conf.urls import url
from rest_framework.routers import DefaultRouter, Route

from license_manager.apps.api.v1 import views


app_name = 'v1'

router = DefaultRouter()  # pylint: disable=invalid-name
router.register(r'subscriptions', views.SubscriptionViewSet, basename='subscriptions')
router.register(r'licenses', views.LicenseViewSet, basename='licenses')

# Add any routes here that can't be easily configured with a Router
urlpatterns = []

urlpatterns += router.urls
