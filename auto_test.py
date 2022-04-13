import unittest
from hypothesis import given
import hypothesis.strategies as st
from hash_map import *

class TestMutableList(unittest.TestCase):
	def test_capacity(self):
		self.assertEqual(hash_map().capacity(), 4)
		self.assertEqual(hash_map([0,1,3,4]).capacity(), 8)
		self.assertEqual(hash_map([0,1,5,9]).capacity(), 12)

	def test_length(self):
		self.assertEqual(hash_map().length(), 0)
		self.assertEqual(hash_map([0,1,3,4]).length(), 4)
		self.assertEqual(hash_map([0,1,5,9]).length(), 4)

	def test_add_value(self):
		self.assertEqual(hash_map().add_value(1).length(), 1)
		self.assertEqual(hash_map([0,1,3,4]).add_value(1).length(), 5)
		
	def test_reduce_value(self):
		self.assertEqual(hash_map().reduce_value(1).length(), 0)
		self.assertEqual(hash_map([0,1,3,4]).reduce_value(1).length(), 3)

	def test_find_value(self):
		self.assertEqual(hash_map().find_value(1), None)
		self.assertEqual(hash_map([0,1,3,4]).find_value(1), 1)

if __name__ == '__main__':
	unittest.main()