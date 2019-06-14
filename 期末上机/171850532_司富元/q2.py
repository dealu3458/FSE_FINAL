#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 10:22:23 2019

@author: dealu_si
"""

num = int(input())
A=[]
B=[]
C=[]
D=[]

for i in range(num):
    ipt = [int(n) for n in input().split()]
    A.append(ipt[0])
    B.append(ipt[1])
    C.append(ipt[2])
    D.append(ipt[3])

sum = 0


for i in range(len(A)):
    for j in range(len(B)):
        for k in range(len(C)):
            for l in range(len(D)):
                if A[i]+B[j]+C[k]+D[l] == 0:
                    sum += 1
                    

print(sum)