#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 10:34:20 2019

@author: dealu_si
"""
ippt = [int(n) for n in input().split()]
n = ippt[0]
k = ippt[1]
num=[]


data=[]
output=[]

for i in range(n):
     buf = [int(n) for n in input().split()]
     data.append(buf)

for i in range(len(data)):
    ai = int(data[i][0])
    bi = int(data[i][1])
    ci = int(data[i][2])
    pivot = int((-1)*(bi/(2*ai)))
    result = int(ai * (pivot * pivot) + bi * pivot + ci)
    num.append(result)
    pivot_dup1 = pivot
    pivot_dup2 = pivot
    for i in range(k):
        pivot_dup1 += 1
        num.append(ai*pivot_dup1*pivot_dup1+bi*pivot_dup1+ci)
    for i in range(k):
        pivot_dup2 -= 1
        num.append(ai*pivot_dup2*pivot_dup2+bi*pivot_dup2+ci)

for i in range(k):
    output.append(min(num))
    num.remove(min(num))


for i in output:
    print(i, end=' ')