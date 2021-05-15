import unittest
from palindrome import is_palidrome

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

"""
def test_positive():
    assert is_palidrome("madam") == True

def test_negative():
    assert is_palidrome("run") == False

def test_phrase():
    assert is_palidrome("nurses run") == True

def test_case():
    assert is_palidrome("MadAM") == True
"""

if __name__ == "__main__":
    unittest.main()
