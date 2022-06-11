import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    """Tests if English to French Works"""
    def test1(self):
        self.assertEqual(english_to_french(" "), " ")
        self.assertEqual(english_to_french("Hello"), "Bonjour")

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        """Tests if French to English works """
        self.assertEqual(french_to_english(" "), " ")
        self.assertEqual(french_to_english("Bonjour"), "Hello")

unittest.main()