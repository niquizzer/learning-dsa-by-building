from sorting import sort

import unittest

class TestSort(unittest.TestCase):
    def test_sort_descending_values_present(self):
        """Test sort for valid list"""
        lst = [5, 4, 3, 1, 2]
        expected = [5, 4, 3, 2, 1]
        actual = sort.sort_descending(lst)

        self.assertEqual(expected, actual)

    def test_sort_descending_empty_list(self):
        """Test sort for empty list"""
        lst = []
        expected = "Empty list"
        actual = sort.sort_descending(lst)

        self.assertEqual(expected, actual)

    def test_sort_descending_wrong_type(self):
        """Test sort for wrong type"""
        lst = ["fizz", "buzz", "cuzz"]
        expected = "Cannot sort strings"
        actual = sort.sort_descending(lst)

        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main(verbosity=2)