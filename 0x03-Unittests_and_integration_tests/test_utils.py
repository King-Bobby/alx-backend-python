#!/usr/bin/env python3
"""Module test_utils.py"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json
from typing import Any, Mapping, Dict, Sequence


class TestAccessNestedMap(unittest.TestCase):
    """Class TestAccessNestedMap"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self,
        nested_map: Mapping,
        path: Sequence,
        expected_result: Any
    ) -> None:
        """Test the access_nested_map function with various inputs"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({}, ("a",), "Key 'a' not found in the nested map"),
        ({"a": 1}, ("a", "b"), "Key 'b' not found in the nested map"),
    ])
    def test_access_nested_map_exception(
        self,
        nested_map: Mapping,
        path: Sequence,
        expected_exception_message: str
    ) -> None:
        """
        Test that access_nested_map
        raises a KeyError with the expected message
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        # Check if the actual exception message matches the expected one
        self.assertEqual(str(context.exception), expected_exception_message)


class TestGetJson(unittest.TestCase):
    """clas TestGetJson"""
    @patch('utils.requests.get')
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload: Any):
        """
        Test the get_json function with mocked requests.get.
        """
        # Create a Mock object for requests.get
        mock_response = Mock()

        # Set the json method of the Mock object to return test_payload
        mock_response.json.return_value = test_payload

        with patch('utils.requests.get',
                   return_value=mock_response) as mock_get:
            result = get_json(test_url)

            # Test that mocked_get method was called exactly once with test_url
            mock_get.assert_called_once_with(test_url)

            # Test that the output of get_json is equal to test_payload
            self.assertEqual(result, test_payload)
