import random
#import community
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
    def __str__(self):
        return "Node " + str(self.idn)
    def __repr__(self):
        return "Node " + str(self.idn)
    
    def copyn(self):
        n= Node(self.idn)
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

class MyIO:
        
    def readLinks(self, s):
        listy = []
        f = open(s, "r")
        lines = f.readlines()
        for line in lines:
            temp = line.split()
            e = Edge(int(temp[0]), int(temp[1]))
            listy.append(e)
        f.close()
        print("number of edges: " + str(self.nedges(listy)))
        print("number of nodes: " + str(self.nnodes(listy))+"\n\n")
        return listy
    def mkadjarray(self, s):
        l = self.readLinks(s)
        listy = {}
        n = self.nnodes(l)
        for i in range(n):
            listy[i] = (Node(i))
        for k in l:
            self.put_node(listy[k.x],k.y)
            self.put_node(listy[k.y],k.x)
        return listy
    
    def nedges(self,listy):
        return len(listy)
    def nnodes(self,listy):
        s= 0
        for n in listy:
            if(s<n.x):
                s=n.x
            if(s<n.y):
                s=n.y
        return s+1
    def put_node(self,n,x):
        temp = n
        while(temp.nextn != None):
            temp = temp.nextn
        temp.nextn = Node(x)
class CommunityDetection:
    
    def __init__(self, s):
        io = MyIO()
        self.listy = io.mkadjarray(s)
        self.n = len(self.listy)
        self.label = list(range(self.n))
        self.cliques = []
        
    def labelPropagation(self):
        order = list(range(self.n))
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
        labels = [0 for i in range(self.n)]
        labels[self.label[node.idn]]+= 1
        node = node.nextn
        while(node != None):
            labels[self.label[node.idn]]+= 1
            node = node.nextn
        return labels.index(max(labels))
    
    
    # Clique Percolation Method
    def CPM(self):
        lbl = 0
        P = []
        for i in range(self.n):
            P.append(self.listy[i])
        self.bronKerbosch( [], P, [])
        for c in self.cliques:
            for n in c:
                self.label[n.idn] = lbl
            lbl = lbl+1
        lencli = len(self.cliques)
        for i in range(lencli):
            for j in range(i+1, lencli):
                if(self.isAdjacentc(self.cliques[i], self.cliques[j])):
                    x = self.label[self.cliques[i][0].idn]
                    for y in self.cliques[j]:
                        self.label[y.idn] = x
        
            
    #finding cliques
    def bronKerbosch(self, R, P, X):
       if((len(P)==0) and (len(X) == 0)):
           self.cliques.append(R)
           return 
       for v in P[:]:
           RR = R[::]
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
            if(self.listy[vv.idn] not in l):
                l.append(self.listy[vv.idn])
            vv = vv.nextn
        return l
    
    def isAdjacentn(self, n1, n2):
        n = n1.copyn()
        n = n.nextn
        while(n != None):
            if(n.idn == n2.idn):
                return True
            n = n.nextn
        
        return False
    
    
    
    def isAdjacentc(self, c1, c2):
        count = 0
        for a in c1:
            for b in c2:
                if(self.isAdjacentn(a,b) == True): #for 2-cliques
                #if(a.idn == b.idn):
                    count+=1
        return (count>3)
    
    # def louvain(self, G):
    #     i = 0
    #     partition = community.best_partition(G)
    #     for c in partition:
    #         for n in c:
    #             self.label[n] = i
    #         i = i+1