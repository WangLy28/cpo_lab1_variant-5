import unittest
from hypothesis import given
import hypothesis.strategies as st
from hash_map_i import *

class TestMutableList(unittest.TestCase):
	def test_capacity(self):
		self.assertEqual(capacity(hash_map()), 4)
		self.assertEqual(capacity(hash_map([0,1,3,4])), 8)
		self.assertEqual(capacity(hash_map([0,1,5,9])), 12)

	def test_length(self):
		self.assertEqual(length(hash_map()), 0)
		self.assertEqual(length(hash_map([0,1,3,4])), 4)
		self.assertEqual(length(hash_map([0,1,5,9])), 4)

	def test_add_value(self):
		self.assertEqual(length(add_value(hash_map(),1)), 1)
		self.assertEqual(length(add_value(hash_map([0,1,3,4]),1)), 5)
		
	def test_reduce_value(self):
		self.assertEqual(length(reduce_value(hash_map(),1)), 0)
		self.assertEqual(length(reduce_value(hash_map([0,1,3,4]),1)), 3)

	def test_find_value(self):
		self.assertEqual(find_value(hash_map(),1), None)
		self.assertEqual(find_value(hash_map([0,1,3,4]),1), 1)

if __name__ == '__main__':
	unittest.main()