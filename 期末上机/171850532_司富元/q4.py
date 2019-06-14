#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 11:28:49 2019
@author: dealu_si
"""

import math

#预处理
input1 = [int(n) for n in input().split()]
nodes_num = input1[0] #nodes_num是节点个数
times = input1[1]
line=[]

for i in range(times):
    ipt = [int(n) for n in input().split()]
    line.append(ipt)
#line是所有的边的列表

#画图,利用line和nodes信息
class Graph():
    def __init__(self,nodeNum,sides,direction=False):
        self.nodeNum = nodeNum #顶点
        self.amatrix = [[0]*(nodeNum+1) for i in range(nodeNum+1)]   #邻接矩阵
        for side in sides:
            u,v,w = side
            if(direction):
                self.amatrix[u][v]=w
            else:
                self.amatrix[u][v]=w
                self.amatrix[v][u]=w

graph = Graph(nodes_num, line, False)


#下面利用上学期学过的还是大一下学过的dijkstra算法解决问题
 
def getMinDistance(graph, v):
    #return结果初始化一下哈
    results = [math.inf] * (graph.nodeNum + 1)
    results[v] = 0
    included = [False] * (graph.nodeNum + 1)
    included[v] = True 
    for i in range(graph.nodeNum + 1):
        if(graph.amatrix[v][i] > 0):
            results[i] = graph.amatrix[v][i]
    
    while(included.count(True) < graph.nodeNum):
        mindata = math.inf
        includenode = 0    #选取未获得最短路径且results[v]最小的结点，源结点到该结点v的最短路径已找到
        for i in range(len(results)):
            if((not math.isinf(results[i])) and (not included[i]) and (mindata > results[i])):
                mindata = results[i]
                includenode = i
        included[includenode]=True
        
        for i in range(graph.nodeNum + 1):   #根据结点v出发的边，更新源结点到v关联的结点的距离
            if(graph.amatrix[includenode][i] > 0):
                newdistance = results[includenode] + graph.amatrix[includenode][i]
                if(newdistance < results[i]):
                    results[i] = newdistance
   
    return results


opt = getMinDistance(graph,1)
print(opt[-1])