'''Test cases for testing the functionality of DistanceCalculator'''

import unittest
from invite import DistanceCalculator

class TestDistanceCalculator(unittest.TestCase):

    def test_incorrect_coordinates(self):
        test_object = DistanceCalculator('gistfile1.txt', "latitude", "longitude", 100.0)
        with self.assertRaises(TypeError):
            test_object.calculate_distance(60, 0) 

    def test_correct_coordinates(self):
        test_object = DistanceCalculator('gistfile1.txt', 42, 22, 100.0)
        self.assertAlmostEqual(round(test_object.calculate_distance(60, 0), 2), 2499.88)

    def test_distance_datatype(self):
        test_object = DistanceCalculator('gistfile1.txt', 42, 22, 100.0)
        self.assertEqual(type(test_object.calculate_distance(60, 0)), float)

    def test_fileinput_incorrectfile(self):
        test_object = DistanceCalculator('incorrectfile.json', 53.3381985, -6.2592576, 100.0)
        with self.assertRaises(FileNotFoundError):
          test_object.fetch_file()
    
    def test_fileinput_correctfile(self):
        test_object = DistanceCalculator('gistfile1.txt', 53.3381985, -6.2592576, 100.0)
        self.assertTrue(test_object.fetch_file())

    def test_negative_distance(self):
        test_object = DistanceCalculator('gistfile1.txt', 42,22, -100.0)
        self.assertFalse(test_object.get_eligible_customers())

    def test_getcustomers(self):
        test_object = DistanceCalculator('gistfile1.txt', 53.3381985, -6.2592576, 100.0)
        self.assertTrue(test_object.get_eligible_customers())

    def test_sorted(self):
        test_object = DistanceCalculator('gistfile1.txt', 53.3381985, -6.2592576, 100.0)
        customers = test_object.get_eligible_customers()
        uid_list = [uid[0] for uid in customers]
        self.assertEqual(uid_list, sorted(uid_list))

if __name__ == '__main__':
    unittest.main()
