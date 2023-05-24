#!/usr/bin/env python3
'''
File: test_utils.py
'''

import unittest
from parameterized import parameterized
from typing import Mapping, Sequence, Any
from utils import access_nested_map


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
