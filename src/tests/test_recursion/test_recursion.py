import unittest
from recursion import counter

class TestRecursion(unittest.TestCase):
    def test_counter(self):
        """Test whether counter returns list"""
        expected = [3, 2, 1]
        actual = counter.recursion_counter()

        self.assertEqual(expected, actual)
