import random
import community
import networkx as nx
import matplotlib.pyplot as plt
class Edge:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
   
        
class Node:
    
    def __init__(self, idn):
        self.idn = idn
        self.nextn = None
        
    def copyn(self):
        n= Node(self.idn)
        n.label=self.label
        if(self.nextn != None):
            n.nextn = self.nextn.copyn()
        return n
    def getDegree(self):
        nod = self.copyn()
        d = 0
        while(nod.nextn != None):
            d = d+1
            nod = nod.nextn  
        return d

class communityDetection:
    
    def __init__(self):
        self.listy = []
        self.n = len(self.listy)
        self.label = range(self.n)
        self.cliques = []
        
    def labelPropagation(self):
        order = range(self.n)
        test = True
        while(test):
            test = False
            random.shuffle(order)
            for i in order:
                if(self.label[i] != self.getLabelMax(self.listy[i])):
                    test = True
                    self.label[i] = self.getLabelMax(self.listy[i])
         

    def getLabelMax(self, nod):
        node = nod.copyn()
        labels = []
        labels.append(self.label[node.idn])
        node = node.nextn
        while(node != None):
            labels.append(self.label[node.idn])
            node = node.nextn
        return max(labels)
    
    
    # Clique Percolation Method
    def CPM(self):
        lbl = 0
        for c in self.cliques:
            for n in c:
                self.label[n.idn] = lbl
            lbl = lbl+1
        for i in range(len(self.cliques)):
            for j in range(i+1, len(self.cliques)):
                if(self.isAdjacentc(self.cliques[i], self.cliques[j])):
                    x = self.label[self.cliques[i][0].idn]
                    for y in self.cliques[j]:
                        self.label[y.idn] = x
        
            
    #finding cliques
    def bronKerbosch(self, R, P, X):
       if((len(P)==0) and len(X) == 0):
           self.cliques.append(R)
           return 0
       for v in P:
           RR = R
           RR.append(v)
           self.bronKerbosch(RR, self.intersection(P, self.N(v)), self.intersection(X, self.N(v)))
           P.remove(v)
           X.append(v)
           
    def intersection(self, lst1, lst2):
        lst3 = [value for value in lst1 if value in lst2] 
        return lst3 
    
    def N(self, v):
        l = []
        vv = v.copyn()
        vv = vv.nextn
        while(vv != None):
            l.append(self.listy[vv.idn])
            vv = v.nextn
        return l
    
    def isAdjacentn(self, n1, n2):
        n = n1.copyn()
        n = n.nextn
        while(n != None):
            if(n == n2):
                return True
        return False
    def isAdjacentc(self, c1, c2):
        for a in c1:
            for b in c2:
                if(self.isAdjacentn(a,b) == True):
                    return True
        return False
    def louvain(self, G):
        i = 0
        partition = community.best_partition(G)
        for c in partition:
            for n in c:
                self.label[n] = i
            i = i+1