#!/usr/bin/env python3

"""This module contains code to solve the
`Parameterize a unit test` task
"""

import unittest
from unittest.mock import patch, Mock
import utils
from parameterized import parameterized
from typing import Dict, Tuple
import requests


class TestAccessNestedMap(unittest.TestCase):
    """The class contains tests for the utils.access_nested_map
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Dict, path: Tuple, expected: any) -> None:
        """Tests utils.access_nested_map"""
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Dict, path: Tuple) -> None:
        """Tests utils.access_nested_map"""
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """"The class contains tests for the utils.get_json
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, test_payload: Dict):
        """Tests utils.get_json"""
        mock = Mock()
        mock.json = lambda: test_payload

        with patch.object(requests, "get", return_value=mock) as mock_method:
            self.assertEqual(utils.get_json(test_url), test_payload)
            mock_method.assert_called_once_with(test_url)
