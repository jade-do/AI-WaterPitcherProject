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

    def test_input_5(self):
        file_path = 'input/input5.txt'
        self.assertEqual(start_search(file_path), 6)

    def test_input_6(self):
        file_path = 'input/input6.txt'
        self.assertEqual(start_search(file_path), 4)

    def test_input_7(self):
        file_path = 'input/input7.txt'
        self.assertEqual(start_search(file_path), 7)

    def test_input_8(self):
        file_path = 'input/input8.txt'
        self.assertEqual(start_search(file_path), 3)

    def test_input_9(self):
        file_path = 'input/input9.txt'
        self.assertEqual(start_search(file_path), 25)

if __name__ == "__main__":
    unittest.main()

