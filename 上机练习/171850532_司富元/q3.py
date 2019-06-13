#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 19:21:37 2019

@author: dealu_si
"""

class Solution(object):
    def stockProfit(input):
        profit = 0
        l = len(input)
        if (l == 1 or l == 0):
            return profit
        else:
            for i in range(1, l):
                sum = input[i] - input[i-1]
                if (sum > 0):
                    profit += sum
        return profit
        