#!/usr/bin/env python3

"""This module contains code to solve the
`Parameterize and patch as decorators` task
"""

import unittest
from unittest.mock import patch, Mock
import utils
from parameterized import parameterized, parameterized_class
from typing import Dict, Tuple
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
import requests


class TestGithubOrgClient(unittest.TestCase):
    """The class contains tests for the
    """

    @parameterized.expand([("google"), ("abc")])
    @patch("client.get_json", return_value={"fake": 0})
    def test_org(self, org: str, mock_method: Mock) -> None:
        """Tests GithubOrgClient.org"""
        new_org = GithubOrgClient(org)
        self.assertEqual(new_org.org, {"fake": 0})
        mock_method.assert_called_once_with(new_org.ORG_URL.format(org=org))

    @patch("client.get_json", return_value=[{"name": "python"}])
    def test_public_repos(self, mock_method: Mock) -> None:
        """Tests GithubOrgClient.org"""
        new_org = GithubOrgClient("google")
        return_value = {"repos_url": {"python": 3}}

        with patch("client.GithubOrgClient._public_repos_url",
                   return_value=return_value) as mocked_property:
            self.assertEqual(new_org.public_repos(), ["python"])
            mock_method.assert_called_once()

    def test_public_repos_url(self) -> None:
        """Tests GithubOrgClient._public_repos_url"""

        return_value = {"repos_url": {"python": 3}}
        with patch("client.get_json", return_value=return_value)\
                as mocked_method:
            new_org = GithubOrgClient("google")
            self.assertEqual(new_org._public_repos_url, {"python": 3})

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: Dict[str, Dict], license: str,
                         expected_value: bool) -> None:
        """Tests GithubOrgClient.test_has_license"""
        self.assertEqual(GithubOrgClient.has_license(
            repo, license), expected_value)


@parameterized_class(("org_payload", "repos_payload",
                      "expected_repos", "apache2_repos"), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests class"""

    @classmethod
    def setUpClass(cls) -> None:
        """Setup class"""
        get_patcher = patch("requests.get").start()
        get_patcher.side_effect

        def side_effect(url: str):
            mock = Mock()
            if url == "https://api.github.com/orgs/google":
                mock.json.return_value = cls.org_payload
            elif url == cls.org_payload["repos_url"]:
                mock.json.return_value = cls.repos_payload
            return mock

        get_patcher.side_effect = side_effect

    @classmethod
    def tearDownClass(cls) -> None:
        """Teardown class"""
        patch("requests.get").stop()

    def test_public_repos(self) -> None:
        """tests public repos function"""
        org = GithubOrgClient("google")
        self.assertEqual(org.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self) -> None:
        """tests public repos with license function"""
        org = GithubOrgClient("google")
        self.assertEqual(org.public_repos(
            license="apache-2.0"), self.apache2_repos)
