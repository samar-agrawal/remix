'''Test the flattening object with some inputs'''

import unittest
from flat import flat

class TestFlat(unittest.TestCase):

    def test_nested_array(self):
        self.assertEqual(flat([[1,2,[3]],4]), [1,2,3,4])

    def test_empty_array(self):
        self.assertIsNone(flat([]))

    def test_multiple_blank_arrays(self):
        self.assertEqual(flat([[[[]]], [], [[]]]), [])

    def test_single_null_integer(self):
        self.assertEqual(flat([0]), [0])

    def test_none(self):
        self.assertEqual(flat([None]), [None])

    def test_nonarray(self):
        self.assertEqual(flat('a'),['a'])

    def mixed_data_structure(self):
        self.assertEqual(flat([[1, [['2']], [[[3]]]],[[4],{5:6}]]), [1, '2', 3, 4, {5: 6}])

    def test_tuple(self):
        self.assertEqual(flat(([1,2,[3]],4)), [1,2,3,4])
    
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
              flat([[[]]], [], [[]])

if __name__ == '__main__':
    unittest.main() 
