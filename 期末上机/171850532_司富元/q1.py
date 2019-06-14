#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 10:02:56 2019

@author: dealu_si
"""

ch = input()
proc = []

while True:
    str = input()
    if str == '@':
        break
    buf = []
    for i in str:
        if not i == ch:
            buf.append(i)
    word =''.join(buf)
    proc.append(word)

for i in range(len(proc)):
    for j in range(i+1, len(proc)):
        if proc[i] < proc[j]:
            var = proc[i]
            proc[i] = proc[j]
            proc[j] = var

for i in proc:
    print(i)
    

