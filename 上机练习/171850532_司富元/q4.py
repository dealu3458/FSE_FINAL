#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 19:33:08 2019

@author: dealu_si
"""
import numpy as np


class Solution(object):
    def ifCross(brick, place):
        sum_ = 0
        for i in range(len(brick)):
            sum_ += brick[i]
            if (place == sum_):
                return True
        return False
    def mimCross(wall):
        cross=[]
        length = np.sum(wall[0])
        for j in range(1, length):
            crossing = 0
            for k in range(len(wall)):
                if not (Solution.ifCross(wall[k], j)):
                    crossing += 1
            cross.append(crossing)
        return min(cross)