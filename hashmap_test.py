import unittest
from hypothesis import given
import hypothesis.strategies as st
from hashmap import *


class TestMutableList(unittest.TestCase):
    def test_capacity(self):
        self.assertEqual(hashMap().capacity(), 4)
        self.assertEqual(hashMap([0, 1, 3, 4]).capacity(), 8)
        self.assertEqual(hashMap([0, 1, 5, 9]).capacity(), 12)

        def test_length(self):
            self.assertEqual(hashMap().length(), 0)
            self.assertEqual(hashMap([0, 1, 3, 4]).length(), 4)
            self.assertEqual(hashMap([0, 1, 5, 9]).length(), 4)

        def test_add_value(self):
            self.assertEqual(hashMap().add_value(1).length(), 1)
            self.assertEqual(hashMap([0, 1, 3, 4]).add_value(1).length(), 4)

        def test_reduce_value(self):
            self.assertEqual(hashMap().reduce_value(1).length(), 0)
            self.assertEqual(hashMap([0, 1, 3, 4]).reduce_value(1).length(), 3)

        def test_find_value(self):
            self.assertEqual(hashMap().find_value(1), None)
            self.assertEqual(hashMap([0, 1, 3, 4]).find_value(1), 1)

        def test_to_list(self):
            self.assertEqual(hashMap().to_list(), [])
            self.assertEqual(hashMap([0, 1, 3, 4]).to_list(), [0, 1, 3, 4])

        def test_from_list(self):
            self.assertEqual(hashMap().from_list([]), None)
            self.assertEqual(hashMap().from_list([0, 1, 3, 4]).table,
                             [4, 1, None, 3, 0, None, None, None])

        def test_map(self):
            self.assertEqual(hashMap().map(str), [None, None, None, None])
            self.assertEqual(hashMap([0, 1, 3, 4]).map(str),
                             ['0', '1', None, '3', '4', None, None, None])

        def test_from_list_to_list_equality(self):
            self.assertEqual(hashMap().from_list([0]).to_list(), [0])

        def test_mempty(self):
            self.assertEqual(hashMap([0, 1, 3, 4]).mempty(),
                             [None, None, None, None])

        def test_mconcat(self):
            self.assertEqual(hashMap([0, 1, 3, 4]).mconcat(hashMap([5]))
                             , [0, 1, None, 3, 4, 5, None, None])


if __name__ == '__main__':
    unittest.main()
