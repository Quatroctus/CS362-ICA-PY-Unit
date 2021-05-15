import unittest
from word_count import word_count

"""
Since the class name starts with the word test and the
functions start with the word test these functions work
in pytest and since the class extends unittest.TestCase
the tests also work for the unittest module.
"""
class TestWordCount(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(word_count(""), 0)

    def test_single(self):
        self.assertEqual(word_count("Hello"), 1)

    def test_multiple(self):
        self.assertEqual(word_count("Hello World!"), 2)

    def test_hyphen(self):
        self.assertEqual(word_count("I'll return it two-fold."), 4)

    def test_whitespace(self):
        self.assertEqual(word_count("    \t\t\r\n"), 0)

if __name__ == "__main__":
    unittest.main()
