"""
Tests for user utils functionality.
"""
from django.test import TestCase
from datetime import datetime
from unittest.mock import patch
from openedx.core.djangoapps.user_authn.views.utils import generate_username_from_request_payload
import ddt


@ddt.ddt
class TestGenerateUsername(TestCase):
    """
    Test case for the generate_username_from_request_payload function.
    """

    @patch('openedx.core.djangoapps.user_authn.views.utils.generate_username')
    def test_generate_username(self, mock_generate_username):
        """
        Test generate_username_from_request_payload function with mock generate_username.
        """

        mock_generate_username.return_value = 'JD_202403_XyZa'
        # Test with known inputs
        data = {'first_name': 'John', 'last_name': 'Doe'}
        username = generate_username_from_request_payload(data)

        self.assertEqual(username, 'JD_202403_XyZa')

    @ddt.data(
        ({'first_name': 'John', 'last_name': 'Doe'}, "JD"),
        ({'name': 'Jane Smith'}, "JS"),
        ({'name': 'Jane'}, "J"),
        ({'name': 'John Doe Smith'}, "JD")
    )
    @ddt.unpack
    def test_generate_username_from_data(self, data, expected_initials):
        """
        Test generate_username_from_request_payload function.
        """
        current_year_month = f"_{datetime.now().year % 100}{datetime.now().month:02d}_"
        username = generate_username_from_request_payload(data)
        expected_username = expected_initials + current_year_month
        self.assertEqual(username[:-4], expected_username)
