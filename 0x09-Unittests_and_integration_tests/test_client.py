#!/usr/bin/env python3
"""Testing the client module
"""

import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD


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

    def test_public_repos_url(self):
        """testing a property
        """
        with patch.object(
                GithubOrgClient, "org", new_callable=PropertyMock)as mock_get:
            mock_get.return_value = {"repos_url": "url_for_mock"}
            test = GithubOrgClient("path")
            self.assertEqual(test._public_repos_url, "url_for_mock")

    @patch("client.get_json", return_value=[{"name": "url_for_mock"}])
    def test_public_repos(self, mock_json):
        """testing the publics repos are correct
        """
        with patch.object(
                GithubOrgClient,
                "_public_repos_url", new_callable=PropertyMock) as mock_url:
            mock_url.return_value = {"name": "url_for_mock"}

            test = GithubOrgClient("url_for_mock")
            repos = test.public_repos()

            self.assertEqual(repos, ["url_for_mock"])

            mock_url.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, dict_keys, linceses, returned):
        """test the metho to get lincese
        """
        checks = GithubOrgClient.has_license(dict_keys, linceses)
        self.assertEqual(checks, returned)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"), [
        (
            TEST_PAYLOAD[0][0],
            TEST_PAYLOAD[0][1],
            TEST_PAYLOAD[0][2],
            TEST_PAYLOAD[0][3]
        )
    ])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """class to test in integration case
    """

    @classmethod
    def setUpClass(cls):
        """set up the instances
        """
        cls.get_patcher = patch("requests.get")
        cls.mock_obj = cls.get_patcher.start()
        cls.mock_obj.side_effect = [(
            cls.org_payload,
            cls.repos_payload,
            cls.expected_repos,
            cls.apache2_repos
        )]

    @classmethod
    def tearDownClass(cls):
        """tear down the instances
        """
        cls.get_patcher.stop()
