#!/usr/bin/env python3.8
'''
File: test_utils.py
'''

import unittest
from parameterized import parameterized
from typing import Mapping, Sequence, Any
from utils import access_nested_map, get_json, memoize
from unittest import mock


class TestAccessNestedMap(unittest.TestCase):
    '''
    Class implements TestAccessNestedMap
    '''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self,
            nested_map: Mapping,
            path: Sequence,
            expected_result: Any
    ) -> None:
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: dict,
            path: tuple
    ):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), "'{}'".format(path[-1]))


class TestGetJson(unittest.TestCase):
    '''
    Class implements TestGetJson
    '''

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @mock.patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        mock_response = mock.Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    '''
    Class implements TestMemoize
    '''
    def test_memoize(self):
        '''
        Test memoization behavior of utils.memoize decorator.
        '''
        class TestClass:
            def a_method(self):
                '''
                Example method.
                '''
                return 42

            @memoize
            def a_property(self):
                '''
                Example property with memoization.
                '''
                return self.a_method()

        with mock.patch('utils.memoize') as mock_memoize:
            mock_memoize.return_value = 42

            test_instance = TestClass()

            result1 = test_instance.a_property
            result2 = test_instance.a_property

            mock_memoize.assert_called_once()
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)


if __name__ == '__main__':
    unittest.main()
