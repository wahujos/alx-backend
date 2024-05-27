#!/usr/bin/env python3
"""
In this task you will write the first unit test for utils.access_nested_map.
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Implement the TestAccessNestedMap.test_access_nested_map
    method to test that the method returns what it is supposed to.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Decorate the method with @parameterized.expand
        to test the function for following inputs:
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a,"), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    
    def test_access_nested_map_exception(self, nested_map, path, missing_key):
        """
        Implement TestAccessNestedMap.test_access_nested_map_exception.
        """
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{missing_key}')", repr(e.exception))


if __name__ == "__main__":
    unittest.main()
