from repeating_vowels import multi_vowel_words
import unittest

class TestRepeatingVowels(unittest.TestCase):
    def test_basic(self):
        testcase = "Life is beautiful"
        expected = ['beautiful']
        self.assertEqual(multi_vowel_words(testcase),expected)
    
    def test_empty(self):
        testcase = " "
        expected = []
        self.assertEqual(multi_vowel_words(testcase),expected)        
    
unittest.main()