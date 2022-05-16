import unittest
from hashmap import hashmap


class TestMutableList(unittest.TestCase):
    def test_capacity(self) -> None:
        '''test capacity'''
        self.assertEqual(hashmap().capacity(), 0)
        self.assertEqual(hashmap([0, 1, 3, 4]).capacity(), 4)

    def test_length(self) -> None:
        '''test length'''
        self.assertEqual(hashmap().length(), 0)
        self.assertEqual(hashmap([0, 1, 3, 4]).length(), 4)
        self.assertEqual(hashmap([0, 1, 3, 4]).reduce(3).length(), 3)

    def test_add(self) -> None:
        '''test add'''
        self.assertEqual(hashmap().add(1), [1])
        self.assertEqual(hashmap([0, 1, 3, 4]).add(1), [0, 1, 4, 3])

    def test_reverse(self) -> None:
        '''test reverse'''
        self.assertIn(hashmap([0, 1, 3, 4]).reverse(),
                      [[3, 4, 1, 0], [0, 1, 3, 4]])

    def test_reduce(self) -> None:
        '''test reduce'''
        self.assertEqual(hashmap().reduce(1), [])
        self.assertEqual(hashmap([0, 1, 3, 4]).reduce(1), [0, None, 4, 3])

    def test_find_value(self) -> None:
        '''test find_value'''
        self.assertEqual(hashmap().find_value(1), 'None')
        self.assertEqual(hashmap([0, 1, 3, 4]).find_value(1), '1')

    def test_to_list(self) -> None:
        '''test to_list'''
        self.assertEqual(hashmap().to_list(), [])
        self.assertIn(hashmap([0, 1]).to_list(), [[0, 1], [1, 0]])

    def test_from_list(self) -> None:
        '''test from_list'''
        self.assertEqual(hashmap().from_list([]), None)
        self.assertIn(hashmap().from_list([0, 1]).table, [[0, 1], [1, 0]])

    def test_map(self) -> None:
        '''test map'''
        self.assertEqual(hashmap().map(str), [])
        self.assertIn(hashmap([0, 1]).map(str), [['0', '1'], ['1', '0']])

    def test_empty(self) -> None:
        '''test empty'''
        self.assertEqual(hashmap([0, 1, 3, 4]).empty(), [])

    def test_mconcat(self) -> None:
        '''test mconcat'''
        self.assertIn(hashmap([0, 1]).mconcat(hashmap([2])),
                      [[0, 1, 2, None], [1, 0, 2, None]])

    def test_filter(self) -> None:
        '''test filter'''
        def isEven(data) -> bool:
            if data % 2 == 0:
                return True
            else:
                return False
        self.assertEqual(hashmap([0, 1, 2]).filter(isEven), [None, 1, None])

    def test_from_list_to_list_equality(self) -> None:
        '''test from_list and to_list'''
        a = [0, 1, 1, 2]
        hm = hashmap()
        hm.from_list(a)
        b = hm.to_list()
        for i in a:
            self.assertIn(i, b)

    def test_python_len_and_capacity_equality(self) -> None:
        '''test len() and capacity'''
        a = [0, 1, 2]
        hm = hashmap()
        hm.from_list(a)
        b = hm.length()
        self.assertEqual(b, len(a))


if __name__ == '__main__':
    unittest.main()
