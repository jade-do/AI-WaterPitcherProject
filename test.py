import unittest
from main import start_search

class TestAStarSearch(unittest.TestCase):

    def test_input_0(self):
        file_path = 'input/input.txt'
        # assert start_search(file_path) == 20, "Should be 20"
        self.assertEqual(start_search(file_path), 20)

    def test_input_1(self):
        file_path = 'input/input1.txt'
        # assert start_search(file_path) == 8, "Should be 8"
        self.assertEqual(start_search(file_path), 8)

    def test_input_2(self):
        file_path = 'input/input2.txt'
        # assert start_search(file_path) == -1, "Should be -1"
        self.assertEqual(start_search(file_path), -1)

    def test_input_3(self):
        file_path = 'input/input3.txt'
        # assert start_search(file_path) == -1, "Should be -1"
        self.assertEqual(start_search(file_path), -1)

    def test_input_4(self):
        file_path = 'input/input4.txt'
        # assert start_search(file_path) == 37, "Should be 37"
        self.assertEqual(start_search(file_path), 37)

if __name__ == "__main__":
    unittest.main()

