import unittest
from palindrome import is_palidrome


"""
Since the class name starts with the word test and the
functions start with the word test these functions work
in pytest and since the class extends unittest.TestCase
the tests also work for the unittest module.
"""
class TestPalindrome(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(is_palidrome("madam"), True)

    def test_negative(self):
        self.assertEqual(is_palidrome("run"), False)

    def test_phrase(self):
        self.assertEqual(is_palidrome("nurses run"), True)

    def test_hyphen(self):
        self.assertEqual(is_palidrome("nurses-run"), True)

    def test_case(self):
        self.assertEqual(is_palidrome("MadAM"), True)

if __name__ == "__main__":
    unittest.main()
