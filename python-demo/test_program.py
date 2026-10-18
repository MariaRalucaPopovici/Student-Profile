import unittest

from MyProgram import greet

class TestProgram(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Maria"), "Hello, Maria!")

if __name__ == "__main__":
    unittest.main()