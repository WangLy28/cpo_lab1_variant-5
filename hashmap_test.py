import unittest
from hashmap import *


class TestMutableList(unittest.TestCase):
    def test_capacity(self) -> None:
        '''test capacity'''
        self.assertEqual(set_hash().capacity(), 0)
        self.assertEqual(set_hash([0, 1, 3, 4]).capacity(), 4)
        self.assertEqual(set_hash([0, 1, 3, 4]).remove(1).capacity(), 4)
        self.assertEqual(set_hash([0, 1, 3, 4]).add(5).capacity(), 8)

    def test_length(self) -> None:
        '''test length'''
        self.assertEqual(set_hash().length(), 0)
        self.assertEqual(set_hash([0, 1, 3, 4]).length(), 4)
        self.assertEqual(set_hash([0, 1, 3, 4]).remove(3).length(), 3)
        self.assertEqual(set_hash([0, 1, 3, 4]).add(5).length(), 5)

    def test_add(self) -> None:
        '''test add'''
        self.assertEqual(set_hash().add(1).length(), 1)
        self.assertEqual(set_hash([0, 1, 3, 4]).add(1).length(), 4)

    def test_reverse(self) -> None:
        '''test reverse'''
        self.assertIn(set_hash([0, 1, 3, 4]).reverse(), [[3, 4, 1, 0], [0, 1, 3, 4]])

    def test_remove(self) -> None:
        '''test remove'''
        self.assertEqual(set_hash().remove(1).length(), 0)
        self.assertEqual(set_hash([0, 1, 3, 4]).remove(1).length(), 3)

    def test_find_value(self) -> None:
        '''test find_value'''
        self.assertEqual(set_hash().find_value(1), False)
        self.assertEqual(set_hash([0, 1, 3, 4]).find_value(1), True)

    def test_to_list(self) -> None:
        '''test to_list'''
        self.assertEqual(set_hash().to_list(), [])
        self.assertIn(set_hash([0, 1]).to_list(), [[0, 1], [1, 0]])

    def test_from_list(self) -> None:
        '''test from_list'''
        self.assertEqual(set_hash().from_list([]), None)
        self.assertIn(set_hash().from_list([0, 1]).table, [[0, 1], [1, 0]])

    def test_map(self) -> None:
        '''test map'''
        self.assertEqual(set_hash().map(str), [])
        self.assertIn(set_hash([0, 1]).map(str), [['0', '1'], ['1', '0']])

    def test_empty(self) -> None:
        '''test empty'''
        self.assertEqual(set_hash([0, 1, 3, 4]).empty(), [])

    def test_mconcat(self) -> None:
        '''test mconcat'''
        self.assertIn(set_hash([0, 1]).mconcat(set_hash([2])), [[0, 1, 2], [1, 0, 2]])

    def test_filter(self) -> None:
        '''test filter'''

        def is_even(data) -> bool:
            if data % 2 == 0:
                return True
            else:
                return False

        self.assertEqual(set_hash([0, 1, 2]).filter(is_even), [1])

    def test_from_list_to_list_equality(self) -> None:
        '''test from_list and to_list'''
        a = [0, 1, 1, 2]
        sethash = set_hash()
        sethash.from_list(a)
        b = sethash.to_list()
        for i in a:
            self.assertIn(i, b)

    def test_python_len_and_capacity_equality(self) -> None:
        '''test len() and capacity'''
        a = [0, 1, 2]
        sethash = set_hash()
        sethash.from_list(a)
        b = sethash.length()
        self.assertEqual(b, len(a))

    def test_python_add_and_remove_equality(self) -> None:
        '''test add and remove'''
        a = set_hash([0, 1, 3, 4]).remove(1).add(1)
        b = set_hash([0, 1, 3, 4])
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()
