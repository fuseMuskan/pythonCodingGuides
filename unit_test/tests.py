import unittest

from unit_test import validate_email_address
from unit_test.stats import calculate_statistics


class TestEmailValidation(unittest.TestCase):
    def test_valid_email(self):
        valid_emails = [
            'john.doe@gmail.com',
            'jane_smith@yahoo.com',
            'user123@outlook.com',
            'john.doe123@example.com',
        ]
        for email in valid_emails:
            with self.subTest(email=email):
                self.assertTrue(validate_email_address(email), f"{email} should be valid.")

    def test_invalid_email_format(self):
        invalid_emails = [
            'invalid_email.com',
            'dunan123@domain',
        ]
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(validate_email_address(email), f"{email} should have an invalid format.")

    def test_invalid_provider(self):
        invalid_emails = [
            'tony.stark@yopmail.com',
            'will_smith@protonmail.com',
        ]
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(validate_email_address(email), f"{email} should have an invalid provider.")


import unittest
import math

class TestCalculateStatistics(unittest.TestCase):

    def test_mean(self):
        dataset = [5, 8, 3, 6, 7, 12, 2, 5]
        result = calculate_statistics(dataset)
        self.assertAlmostEqual(result["mean"], 6.125, places=3)

    def test_median_odd_length(self):
        dataset = [5, 8, 3, 6, 7, 12, 2, 5]
        result = calculate_statistics(dataset)
        self.assertEqual(result["median"], 5.5)

    def test_median_even_length(self):
        dataset = [5, 8, 3, 6, 7, 12, 2, 5, 9]
        result = calculate_statistics(dataset)
        self.assertEqual(result["median"], 6)

    def test_standard_deviation(self):
        dataset = [5, 8, 3, 6, 7, 12, 2, 5]
        result = calculate_statistics(dataset)
        self.assertAlmostEqual(result["standard_deviation"], math.sqrt(10.0625), places=3)

    def test_empty_dataset(self):
        dataset = []
        result = calculate_statistics(dataset)
        self.assertEqual(result, "Dataset cannot be empty")

    def test_single_element_dataset(self):
        dataset = [5]
        result = calculate_statistics(dataset)
        self.assertEqual(result, "Please provide more than one element in the dataset")

if __name__ == '__main__':
    unittest.main()



if __name__ == '__main__':
    unittest.main()
