#!/usr/bin/env python3
"""Testing the client module
"""

import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """class to rest the github class
    """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json")
    def test_org(self, values, mock_json):
        """test the correct org
        """
        test = GithubOrgClient(values)
        test.org
        mock_json.assert_called_once_with(
            GithubOrgClient.ORG_URL.format(org=values))
