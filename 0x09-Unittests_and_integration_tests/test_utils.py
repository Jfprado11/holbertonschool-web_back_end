#!/usr/bin/env python3
""" first testing
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json


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

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, map, path, err):
        """test if an error has raises
        """
        with self.assertRaises(KeyError) as er:
            access_nested_map(map, path)
        self.assertEqual(er.exception.args[0], err)


class TestGetJson(unittest.TestCase):
    """Testing the json get function with mock
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url_test, data):
        """testing the get json
        """
        with patch("utils.requests.get") as mock_req:
            mock_req.return_value = mock_req
            mock_req.json.return_value = data
            data_json = get_json(url_test)
            mock_req.assert_called_once_with(url_test)
            self.assertEqual(data, data_json)
