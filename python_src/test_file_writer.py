import unittest
import os
from file_writer import FileWriter


class TestFileWriter(unittest.TestCase):

    def setUp(self):
        self.filename = "test_output.txt"
        self.file_writer = FileWriter(self.filename)

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_write_single_value(self):
        data = [42]
        self.file_writer.write(data)

        with open(self.filename, "r") as file:
            content = file.read().strip()

        self.assertEqual(content, "42")

    def test_write_list_of_values(self):
        data = [[1, 2, 3], [4, 5, 6]]
        self.file_writer.write(data)

        with open(self.filename, "r") as file:
            lines = file.readlines()

        self.assertEqual(lines[0].strip(), "1 2 3")
        self.assertEqual(lines[1].strip(), "4 5 6")

    def test_write_mixed_values(self):
        data = [7, [8, 9], 10]
        self.file_writer.write(data)

        with open(self.filename, "r") as file:
            lines = file.readlines()

        self.assertEqual(lines[0].strip(), "7")
        self.assertEqual(lines[1].strip(), "8 9")
        self.assertEqual(lines[2].strip(), "10")


if __name__ == "__main__":
    unittest.main()
