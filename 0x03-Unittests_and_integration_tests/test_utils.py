#!/usr/bin/env python3
"""Module test_utils.py"""

import unittest
from parameterized import parameterized
from utils import access_nested_map
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
        Test that access_nested_map raises a KeyError with the expected message
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        # Check if the actual exception message matches the expected one
        self.assertEqual(str(context.exception), expected_exception_message)
