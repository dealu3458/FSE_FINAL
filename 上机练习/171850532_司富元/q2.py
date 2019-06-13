#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 19:15:16 2019

@author: dealu_si
"""

class Solution(object):
    def bigSum(a, b):
        if a == 0:
            return b
        if b == 0:
            return a
        c = 1
        d = 1
        c = a^b
        d = (a&b)<<1
        return Solution.bigSum(c, d)