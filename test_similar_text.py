# -*- coding: utf-8 -*-

import unittest
from similar_text import similar_text

class TestStringMethods(unittest.TestCase):
    def test_similar(self):
        case1 = similar_text('aaaa', 'aaaa')
        case2 = similar_text('aaaa', 'bbbb')
        case3 = similar_text('abcdef', 'aabcdefg')
        case4 = similar_text('lsc', 'luosch')
        case5 = similar_text('lsc', 'zyl')
        case6 = similar_text(u'习近平', u'习惯')

        self.assertTrue(case1 == 100)
        self.assertTrue(case2 == 0)
        self.assertTrue(case3 == 85)
        self.assertTrue(case4 == 66)
        self.assertTrue(case5 == 33)
        self.assertTrue(case6 == 40)

    def test_similar_option(self):
        self.assertRaises(TypeError, similar_text, 1, 2)
        self.assertRaises(TypeError, similar_text, [1, 2, 3], {3, 2, 1})

if __name__ == '__main__':
    unittest.main()