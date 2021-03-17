# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 11:01:20 2021

@author: Belkacem GUELIANE & Jae-Soo LEE
"""
from tme3Opt import * 
import time
import tme3graphGenOpt
#from tm3grapheGen import *



#creating EdgeList and AdjArray (also AdjMatrix but it's not scalable so it's commented out)
start = time.time()
g = Graph("test.txt")
l = g.mkEdgeList()
#m = g.mkAdjMatrix(l)
a = g.mkAdjArray(l)
end = time.time()
print("creating EdgeList + AdjArray time is: "+ str(end-start)+"\n")

#running the algorithms for community detection
gf = FourClusterGraph(0.07, 0.0008)
cd = CommunityDetection(g.mkAdjArray(gf.exportGraph()))
cd = CommunityDetection(a)
# cd.labelPropagation()
cd.CPM()
print(cd.label)
print(set(cd.label))

#frawing the colored graph
#g.drawGraph(cd.label)














