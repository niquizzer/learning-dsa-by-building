import unittest

def read_50_lines_then_reverse(path:str) -> list[str]:
    """Reads 50 lines then reverses it for whole text."""
    result = []
    with open(path, "r") as f:
        lst = []

        for row,val in enumerate(f):
            val = val.strip()
            lst.append(val)

            if (row + 1) % 50 == 0:
                lst[(row+1)-50:row].reverse()

    return lst 


class TestRead50(unittest.TestCase):
    def test_read_50(self):
        path = "demo-2.txt"
        result = "result-2.txt"

        with open(result, 'r') as f:
            lst = []
            for row in f:
                row = row.strip()
                lst.append(row)
        
        self.assertEqual(read_50_lines_then_reverse(path), lst)

if __name__ == "__main__":
    unittest.read_50_lines_then_reverse()