# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 11:01:20 2021

@author: Belkacem GUELIANE & Jae-Soo LEE
"""

import numpy as np
import random as rd
import networkx as nx
import matplotlib.pyplot as plt
import pygraphviz
import community as c


class Edge:
    __slots__ = 'x', 'y'
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        
    
class Node:
    __slots__ = 'idn', 'neighbours'
    def __init__(self, idn):
        self.idn = idn
        self.neighbours = []

        
    def copyn(self):
        n= Node(self.idn)
        n.neighbors = self.neighbors[:]
        return n
    
    @property
    def d(self):
        return len(self.neighbours)

       
class Cluster:
    
    def __init__(self, idc, nodes):
        self.idc = idc
        self.nodes = []
        

class FourClusterGraph:
    
    def __init__(self, p, q):
        rd.seed()
        self.p = p
        self.q = q
        self.com = []
        self.edges = []
        self.cl1 = Cluster(1, [])
        self.cl2 = Cluster(2, [])
        self.cl3 = Cluster(3, [])
        self.cl4 = Cluster(4, [])
        self.nodes = []
        for i in range(400):
            self.nodes.append(Node(i))
        print(len(self.nodes))
        for j in range(100):
            self.cl1.nodes.append(self.nodes[j])
            self.cl2.nodes.append(self.nodes[j + 100])
            self.cl3.nodes.append(self.nodes[j + 200])
            self.cl4.nodes.append(self.nodes[j + 300])
            
            
            
    def proba_add(self, p, n1, n2):
            rd.seed()
            if rd.random() <= p:
                self.edges.append(Edge(n1, n2))
    def exportGraph(self):
        self.fill_intraEdge()
        self.fill_extraEdge()
        
        l = []
        for e in self.edges:
            l.append(Edge(e.x.idn, e.y.idn))
        return l
        
    def fill_intraEdge(self):
            for i in range(100):
                for j in range(i + 1, 100, 1):
                    self.proba_add(self.p, self.cl1.nodes[i], self.cl1.nodes[j])
                    self.proba_add(self.p, self.cl2.nodes[i], self.cl2.nodes[j])
                    self.proba_add(self.p, self.cl3.nodes[i], self.cl3.nodes[j])
                    self.proba_add(self.p, self.cl4.nodes[i], self.cl4.nodes[j])
                    
    def add_interEdge(self, cluster1, cluster2):
            for i in range(100):
                for j in range(100):
                    self.proba_add(self.q, cluster1.nodes[i], cluster2.nodes[j])
                    
    def fill_extraEdge(self):
            self.add_interEdge(self.cl1, self.cl2)
            self.add_interEdge(self.cl1, self.cl3)
            self.add_interEdge(self.cl1, self.cl4)
            self.add_interEdge(self.cl2, self.cl3)
            self.add_interEdge(self.cl2, self.cl4)
            self.add_interEdge(self.cl3, self.cl4)
            
    def colorMapping(self, com):
        commuSet = set(com)
        i =0
        commuDict = {}
        for c in commuSet:
            commuDict[c] = i
            i = i+100
        colors = []
        for comm in com:
            colors.append(commuDict[comm])
        return colors



    def drawCorrectGraph(self):
            G = nx.Graph()
            color_map = []
            pos = nx.nx_agraph.graphviz_layout(G)
            for i in range(100):
                G.add_nodes_from([self.cl1.nodes[i].idn], node_color = 'red')
                color_map.append(0)
                G.add_nodes_from([(self.cl2.nodes[i].idn, {"color":"blue"})])
                color_map.append(4)
                G.add_nodes_from([(self.cl3.nodes[i].idn, {"color":"green"})])
                color_map.append(8)
                G.add_nodes_from([(self.cl4.nodes[i].idn, {"color": "yellow"})])
                color_map.append(12)
            graphEdges = []
            for j in self.edges:
                graphEdges.append((j.x.idn, j.y.idn))
            G.add_edges_from(graphEdges)
            nx.draw_networkx(G,  pos = nx.nx_agraph.graphviz_layout(G), with_labels=False,edgelist = graphEdges,node_color = color_map, node_size = 10, font_weight='bold')
            plt.show()
            
    def drawGraph(self, com):
            self.com = com
            G = nx.Graph()
            pos = nx.nx_agraph.graphviz_layout(G)
            for i in range(100):
                G.add_node(self.cl1.nodes[i].idn)
            for i in range(100):
                G.add_node(self.cl2.nodes[i].idn)
            for i in range(100):
                G.add_node(self.cl3.nodes[i].idn)
            for i in range(100):
                G.add_node(self.cl4.nodes[i].idn)
            graphEdges = []
            for j in self.edges:
                graphEdges.append((j.x.idn, j.y.idn))
            G.add_edges_from(graphEdges)
            nx.draw_networkx(G,  pos = nx.nx_agraph.graphviz_layout(G), with_labels=False,edgelist = graphEdges,node_color = com, node_size = 10, font_weight='bold')
            plt.show()


#pos = nx.nx_agraph.graphviz_layout(G, prog = 'sfdp')









            
       