import unittest

def reverse_lines(path:str) -> list[str]:
    """Reads text file and reverses it.

    Args:
        path(str): is the file path for file.
        
    Returns:
        list(str): is the text file reversed
        with each line a new index."""
    lst = []
    
    with open(path, 'r') as fh:
        for row in fh:
            row = row.strip("\n")
            lst.append(row)

    lst.reverse()
    return lst


class TestReverseLines(unittest.TestCase):
    def test_reversed_lines(self):
        lines = "demofile.txt"
        expected_result = ["Good Luck!", "This file is for testing purposes.", "Hello! Welcome to demofile.txt"]
        self.assertEqual(reverse_lines(lines), expected_result)

if __name__ == "__main__":
    unittest.reverse_lines()