import unittest
from quick_sort import qsort

class TestQuickSort(unittest.TestCase):
    def test_empty_list(self):
        lst = []
        expected = [] 
        self.assertEqual(expected, qsort.qsort(lst))

    def test_one_item(self):
        lst = [-7]
        expected = [-7]
        self.assertEqual(expected, qsort.qsort(lst))

    def test_two_items(self):
        lst = [8, -3]
        expected = [-3, 8]
        self.assertEqual(expected, qsort.qsort(lst))

    def test_three_items(self):
        lst = [4, 4, 1]
        expected = [1, 4, 4]
        self.assertEqual(expected, qsort.qsort(lst))

    def test_ten_items(self):
        lst = [12, -4, 7, 0, 12, -9, 3, 7, 1, -1]
        expected = [-9, -4, -1, 0, 1, 3, 7, 7, 12, 12]
        self.assertEqual(expected, qsort.qsort(lst))
        