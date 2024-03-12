"""
Tests for the utility functions defined as part of the credentials app's public Python API.
"""


from django.test import TestCase

from openedx.core.djangoapps.credentials.api import is_credentials_enabled
from openedx.core.djangoapps.credentials.models import CredentialsApiConfig
from openedx.core.djangoapps.credentials.tests.mixins import CredentialsApiConfigMixin


class CredentialsApiTests(CredentialsApiConfigMixin, TestCase):
    """
    Tests for the Public Pyton API exposed by the credentials Django app.
    """

    def setUp(self):
        super().setUp()

    def tearDown(self):
        CredentialsApiConfig.objects.all().delete()
        super().tearDown()

    def test_is_credentials_enabled_config_enabled(self):
        """
        A test that verifies the output of the `is_credentials_enabled` utility function when a CredentialsApiConfig
        exists and is enabled.
        """
        self.create_credentials_config(enabled=True)
        assert is_credentials_enabled()

    def test_is_credentials_enabled_config_disabled(self):
        """
        A test that verifies the output of the `is_credentials_enabled` utility function when a CredentialsApiConfig
        exists and is disabled.
        """
        self.create_credentials_config(enabled=False)
        assert not is_credentials_enabled()

    def test_is_credentials_enabled_config_absent(self):
        """
        A test that verifies the output of the `is_credentials_enabled` utility function when a CredentialsApiConfig
        does not exist.
        """
        assert not is_credentials_enabled()
