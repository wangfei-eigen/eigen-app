#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Authour wangfei

import  unittest
assert 1==1
class TestA(unittest.TestCase):

    def test_say_hi(self):
        self.assertEqual(1, 1)