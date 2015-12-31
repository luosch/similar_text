# -*- coding: utf-8 -*-

import unittest
from similar_text import similar_text

class TestStringMethods(unittest.TestCase):
    def test_similar_normal(self):
        case1 = similar_text('aaaa', 'aaaa')
        case2 = similar_text('aaaa', 'bbbb')
        case3 = similar_text('abcdef', 'aabcdefg', 'normal')

        self.assertTrue(int(case1) == 100)
        self.assertTrue(int(case2) == 0)
        self.assertTrue(int(case3) == 85)

    def test_similar_fast(self):
        case1 = similar_text('aaaa', 'aaaa', 'fast')
        case2 = similar_text('aaaa', 'bbbb', 'fast')
        case3 = similar_text('abcdef', 'aabcdefg', 'fast')

        self.assertTrue(int(case1) == 100)
        self.assertTrue(int(case2) == 0)
        self.assertTrue(int(case3) == 71)

    def test_similar_option(self):
        self.assertRaises(ValueError, similar_text, 'aaaa', 'aaaa', 'very fast')

if __name__ == '__main__':
    unittest.main()