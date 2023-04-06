import unittest
import translator

class TestTranslator(unittest.TestCase):
    def test_e2f(self):
        text = 'Hello'
        tran = translator.english_to_french(text)

        self.assertEqual(tran, 'Bonjour')
        self.assertNotEqual(tran, text)

    def test_e2f_null(self):
        text = ''
        tran = translator.english_to_french(text)

        self.assertEqual(tran, '')
        self.assertNotEqual(tran, 'Bonjour')

    def test_f2e(self):
        text = 'Bonjour'
        tran = translator.french_to_english(text)

        self.assertEqual(tran, 'Hello')
        self.assertNotEqual(tran, text)

    def test_f2e_null(self):
        text = ''
        tran = translator.french_to_english(text)

        self.assertEqual(tran, '')
        self.assertNotEqual(tran, 'Hello')

if __name__ == '__main__':
    unittest.main()