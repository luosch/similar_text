import unittest
from source.similar_text import similar_text

class TestStringMethods(unittest.TestCase):
    def test_similar_normal(self):
        case1 = similar_text('aaaa', 'aaaa')
        self.assertTrue(int(case1) == 100)

    def test_similar_option(self):
        self.assertRaises(ValueError, similar_text, 'aaaa', 'aaaa', 'very fast')

if __name__ == '__main__':
    unittest.main()