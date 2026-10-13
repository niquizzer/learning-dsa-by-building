import unittest

from binary_search import search 

class TestLinearSearch(unittest.TestCase):
    def test_successful_linear_search(self):
        """Test for successful search."""
        path = "data/sorted_unique.txt"
        target = 32335861

        self.assertEqual(search.linear_search(path, target), target)

    def test_unsuccessful_linear_search(self):
        """Test for unsuccessful search."""
        path = "data/sorted_unique.txt"
        target = 0
        error = -1

        self.assertEqual(search.linear_search(path, target), error)

    def test_searching_empty_linear_list(self):
        """Test for empty list."""
        path = "data/empty_list.txt"
        target = 32335861
        error = -99

        self.assertEqual(search.linear_search(path, target), error)

    def test_unsorted_list(self):
        """Test for unsorted list."""
        path = "data/unsorted_unique.txt"
        target = 32335861

        self.assertEqual(search.linear_search(path, target), target)

if __name__ == "__main__":
    unittest.main(verbosity=2)