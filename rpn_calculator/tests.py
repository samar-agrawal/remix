'''Test cases for testing the functionality of DistanceCalculator'''

import unittest
from rpn_calculator import process

class TestRPNCalculator(unittest.TestCase):

    def test_basic_operator(self):
        self.assertEqual(process("1 3 +"), 4)
        self.assertEqual(process("5 3 -"), 2)
        self.assertEqual(process("2 4 *"), 8)
        self.assertEqual(process("6 2 /"), 3)

    def test_equation(self):
        self.assertEqual(process("1 3 + 5 3 - *"), 8)

    def test_invalid_operator(self):
        with self.assertRaises(TypeError):
            process("1 3 ? 5 3 - *")

    def test_invalid_equation(self):
        with self.assertRaises(TypeError):
            process("3 − 4 + 5")

if __name__ == '__main__':
    unittest.main()
