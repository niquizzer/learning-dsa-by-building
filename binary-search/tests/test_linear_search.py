import unittest

class TestLinearSearch(unittest.TestCase):
    def test_successful_linear_search(self):
        path = "data/sorted_unique.txt"
        target = 32335861

        self.assertEqual(linear_search(path, target), target)

    def test_unsuccessful_linear_search(self):
        path = "data/sorted_unique.txt"
        target = 0
        error = -1

        self.assertEqual(linear_search(path, target), error)

    def test_searching_empty_linear_list(self):
        path = "data/empty_list.txt"
        target = 32335861
        error = -99

        self.assertEqual(linear_search(path, target), error)

    def test_unsorted_list(self):
        path = "data/unsorted_unique"
        target = 32335861

        self.assertEqual(linear_search(path, target), target)
