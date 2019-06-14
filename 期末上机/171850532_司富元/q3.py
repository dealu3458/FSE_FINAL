#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 11:43:26 2019

@author: dealu_si
"""

nodesNum = input()
line=[]

for i in range(nodesNum-1):
    buf = [int(n) for n in input().split()]
    line.append(buf)
#输入完成
    
    #画图,利用line和nodes信息
class Graph():
    def __init__(self,nodeNum,sides,direction=False):
        self.nodeNum = nodeNum #顶点
        self.amatrix = [[0]*(nodeNum+1) for i in range(nodeNum+1)]   #邻接矩阵
        for side in sides:
            u,v,w = side
            if(direction):
                self.amatrix[u][v]=w

graph = Graph(nodesNum, line, False)

