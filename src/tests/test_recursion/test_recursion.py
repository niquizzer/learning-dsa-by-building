import unittest
from recursion import counter

class TestRecursion(unittest.TestCase):
    def test_counter(self):
        """Test whether counter returns list"""
        expected = [3, 2, 1]
        actual = counter.recursion_counter()

        self.assertEqual(expected, actual)
    def test_factorial(self):
        """Test whether counter returns list"""
        num = 5
        expected = 120  
        actual = counter.calculate_factorial(num)

        self.assertEqual(expected, actual)

    def test_sum(self):
        lst = [1, 2, 3]
        expected = 6
        actual = counter.recursive_sum(lst)

        self.assertEqual(expected, actual)

    def test_count_item(self):
        mixed_list = [
            42, -7, 0, 3.14, -2.5, 1e6,
            "hello", "", "123", 'a',
            True, False, None,
            [1, 2, 3], [], [[4, 5], 6],
            (7, 8), {"key": "value"}, {1, 2, 3},
            b"bytes", complex(2, 3),
            range(5), 99, "world", 0.0, -100
        ]

        expected = 26
        actual = counter.count_list_items(mixed_list)

        self.assertEqual(expected, actual)
