import numpy as np
import random as rd
import networkx as nx
import matplotlib.pyplot as plt

class Edge:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Node:
    
    def __init__(self, idn):
        self.idn = idn

        
class Cluster:
    
    def __init__(self, idc, nodes):
        self.idc = idc
        self.nodes = []
        


class Graph:
    
    def __init__(self, p, q):
        rd.seed()
        self.p = p
        self.q = q
        self.edges = []
        self.cl1 = Cluster(1, [])
        self.cl2 = Cluster(2, [])
        self.cl3 = Cluster(3, [])
        self.cl4 = Cluster(4, [])
        self.nodes = []
        for i in range(400):
            self.nodes.append(Node(i))
        for j in range(100):
            self.cl1.nodes.append(self.nodes[i])
            self.cl2.nodes.append(self.nodes[i + 100])
            self.cl3.nodes.append(self.nodes[i + 200])
            self.cl4.nodes.append(self.nodes[i + 300])
        # for i in range(100):
        #     for j in range(i + 1, 100, 1):
        #         rNb1 = rd.random()
        #         rNb2 = rd.random()
        #         rNb3 = rd.random()
        #         rNb4 = rd.random()
        #         if rNb1 <= p:
        #             self.edges.append(Edge(self.cl1.nodes[i], self.cl1.nodes[j]))
        #         if rNb2 <= p
        #             self.edges.append(Edge(self.cl2.nodes[i], self.cl2.nodes[j]))
        #         if rNb3 <= p
        #             self.edges.append(Edge(self.cl3.nodes[i], self.cl3.nodes[j]))
        #         if rNb4 <= p                    
        #             self.edges.append(Edge(self.cl4.nodes[i], self.cl4.nodes[j]))
        # for i in range(100):
            
        def proba_add(p, n1, n2):
            rd.seed();
            if rd.random() <= p:
                self.edges.append(n1, n2)
            
        def fill_intraEdge():
            for i in range(100):
                for j in range(i + 1, 100, 1):
                    proba_add(self.p, self.cl1.nodes[i], self.cl1.nodes[j])
                    proba_add(self.p, self.cl2.nodes[i], self.cl2.nodes[j])
                    proba_add(self.p, self.cl3.nodes[i], self.cl3.nodes[j])
                    proba_add(self.p, self.cl4.nodes[i], self.cl4.nodes[j])
                    
        def add_interEdge(cluster1, cluster2):
            for i in range(100):
                for j in range(100):
                    proba_add(self.q, cluster1.nodes[i], cluster2.nodes[j])
                    
        def fill_extraEdge():
            add_interEdge(self.cl1, self.cl2)
            add_interEdge(self.cl1, self.cl3)
            add_interEdge(self.cl1, self.cl4)
            add_interEdge(self.cl2, self.cl3)
            add_interEdge(self.cl2, self.cl4)
            add_interEdge(self.cl3, self.cl4)        



        def draw_graph(self):
            G = nx.Graph()
            for i in range(100):
                G.add_node(self.cl1.nodes[i].idn, {"color": "red"})
                G.add_node(self.cl2.nodes[i].idn, {"color": "blue"})
                G.add_node(self.cl3.nodes[i].idn, {"color": "green"})
                G.add_node(self.cl4.nodes[i].idn, {"color": "yellow"})
            for j in self.edges:
                G.add_edge(j.x, j.y)
            nx.draw(G, with_labels=True, font_weight='bold')
            plt.show()






G = Graph(0.7, 0.2)

G.fill_intraEdge()
G.fill_extraEdge()

G.draw_graph()





            
            