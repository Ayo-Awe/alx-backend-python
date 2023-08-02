#!/usr/bin/env python3

"""This module contains code to solve the
`Parameterize and patch as decorators` task
"""

import unittest
from unittest.mock import patch, Mock
import utils
from parameterized import parameterized
from typing import Dict, Tuple
from client import GithubOrgClient


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
        with patch("client.get_json", return_value=return_value) as mocked_method:
            new_org = GithubOrgClient("google")
            self.assertEqual(new_org._public_repos_url, {"python": 3})
