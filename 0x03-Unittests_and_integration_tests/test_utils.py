#!/usr/bin/env python3

"""This module contains code to solve the
`Parameterize a unit test` task
"""

import unittest
import utils
from parameterized import parameterized
from typing import Dict, Tuple


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
