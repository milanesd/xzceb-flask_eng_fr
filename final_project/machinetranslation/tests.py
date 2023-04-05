import unittest
import translator

class TestTranslator(unittest.TestCase):
    def test_e2f(self):
        str = translator.english_to_french('')
        self.assertEqual(str, '')

        str = translator.english_to_french('Hello')
        self.assertEqual(str, 'Bonjour')

    def test_f2e(self):
        str = translator.french_to_english('')
        self.assertEqual(str, '')

        str = translator.french_to_english('Bonjour')
        self.assertEqual(str, 'Hello')

if __name__ == '__main__':
    unittest.main()