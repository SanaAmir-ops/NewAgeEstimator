import unittest
from PythonAgeEstimate import calculate_age

class TestAgePredictor(unittest.TestCase):
    def test_age_calculation(self):
        self.assertEqual(calculate_age('2000-01-01'), 23)  # Adjust the expected age based on the current year

if __name__ == '__main__':
    unittest.main()
