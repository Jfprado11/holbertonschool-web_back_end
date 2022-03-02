#!/usr/bin/env python3
""" first testing
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Testing a function for mapping
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map,  path, result):
        """testing if the value is correct
        """
        nested_result = access_nested_map(map, path)
        self.assertEqual(nested_result, result)
