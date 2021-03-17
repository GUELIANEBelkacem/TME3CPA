# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 11:01:20 2021

@author: Belkacem GUELIANE & Jae-Soo LEE
"""
import random


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

    
        
        
class Graph:
    """ class Graph(String s) takes the path to the .txt file containing a list of edges.
        \n contains methids for generating an Edge List, an Adjacency Matrix and/or 
        an Adjacency Array, along with print methodes for all 3 data structures"""
    def __init__(self, s):
        self.s = s
        
    #data structure makers--------------------------------------------------
    
    def mkEdgeList(self):
        """ mkEdgeList() makes an edge list from the given .txt file inserted when creating an instance of Graph""" 
        listy = []
        f = open(self.s, "r")
        lines = f.readlines()
        for line in lines:
            temp = line.split()
            e = Edge(int(temp[0]), int(temp[1]))
            listy.append(e)
        f.close()
        print("number of edges: " + str(self.nedges(listy)))
        print("number of nodes: " + str(self.nnodes(listy))+"\n\n")
        return listy
    
    
    
    
    def mkAdjMatrix(self, l):
        """ mkAdjMatrix(EdgeList l) makes an adjacincy matrix from a given edge list""" 
        n = self.nnodes(l)
        matrix = [ [ 0 for i in range(n) ] for j in range(n) ] 
        for e in l:
            matrix[e.x][e.y] = 1
        return matrix
    
    
    
    
    def mkAdjArray(self,l):
        """ mkAdjArray(EdgeList l) makes an adjacincy array from a given edge list""" 
        
        listy = {}
        n = self.nnodes(l)
        for i in range(n):
            listy[i] = (Node(i))
        for k in l:
            listy[k.x].neighbours.append(k.y)
            listy[k.y].neighbours.append(k.x)
        return listy
    

    
    
    def mkadjarray2(self, l):
        """ mkAdjArray2(EdgeList l) makes an adjacincy array from a given edge list 
        with the particulatity of it turned into a directed graph 
        (useful for detecting triangles)""" 
        listy = {}
        n = self.nnodes(l)
        for i in range(n):
            listy[i] = (Node(i))
        for k in l:
            listy[k.x].neighbours.append(k.y)

        return listy
    
            
    #support functions------------------------------------------------------                     
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
    
    #prints-----------------------------------------------------------------
    def print_edges(self, listy):
        f = open("EdgeList.txt", "w")
        for e in listy:
            f.write(str(e.x)+"   "+str(e.y)+"\n")
        f.close()    
    def print_matrix(self, matrix):
        f = open("AdjMatrix.txt", "w")
        s = ""
        f.write("the adjacency matrix:\n")
        s = ""
        for i in matrix:
            for j in i:
                s= s+(str(j) + " ")
            s= s+("\n")
            f.write(s)
        
        f.close() 
        
    def print_adjarray(self, listy):
        f = open("AdjArray.txt", "w")
        s = ""
        print("the adjacency array:\n")
        for i in listy:
            n = listy[i]
            s = ""
            s = s+str(n.idn)+" -> "            
            for neighbour in n.neighbours:
                s = s+str(neighbour)+" -> "
            s = s+"/\n"
            f.write(s)
            #print(s)
        f.close()
        

class CommunityDetection:
    __slots__ = 'adjarr', 'n', 'label', 'cliques'
    
    def __init__(self, adjarr):
        self.adjarr = adjarr
        self.n = len(self.adjarr)
        self.label = list(range(self.n))
        self.cliques = []
        
    def labelPropagation(self):
        """ labelPropagation() uses the label propagation algorithm to find 
        communities, outputs a dictionary relaying a label to each node""" 
        order = list(range(self.n))
        test = True
        while(test):
            test = False
            random.shuffle(order)
            for i in order:
                if(self.label[i] != self.getLabelMax(self.adjarr[i])):
                    test = True
                    self.label[i] = self.getLabelMax(self.adjarr[i])
         

    def getLabelMax(self, node):
        labels = [0 for i in range(self.n)]
        labels[self.label[node.idn]]+= 1
        for nei in node.neighbours:
            labels[self.label[nei]]+= 1
        return labels.index(max(labels))
    
    
  
    
    def CPM(self):
        """ CPM() uses the Clique Percolation algorithm to find 
        communities, outputs a dictionary relaying a label to each node""" 
        lbl = 1
        #--------
        freq = {}
        for i in range(self.n):
            freq[i] = []
        P = []
        #--------------
        for i in range(self.n):
            P.append(self.adjarr[i])
        self.bronKerbosch( [], P, [])
        for c in self.cliques:
            for n in c:
                self.label[n] = lbl
                freq[n].append(lbl)
            lbl = lbl+1
        lencli = len(self.cliques)
        for i in range(lencli):
            for j in range(lencli):
                if(self.isAdjacentc(self.cliques[i], self.cliques[j])):
                    x = self.label[self.cliques[i][0]]
                    for y in self.cliques[j]:
                        #self.label[y.idn] = x
                        freq[y].append(x)

        for i in range(self.n ):
            self.label[i] = self.most_frequent(freq[i])
                        
                        
                        
                        
    def most_frequent(self, List): 
        
        if(not(List)):
            return 0
        counter = 0
        num = List[0] 
    
        for i in List: 
            curr_frequency = List.count(i) 
            if(curr_frequency> counter): 
                counter = curr_frequency 
                num = i 
    
        return num 
        
            
    #finding cliques
    def bronKerbosch(self, R, P, X):
        """ bronKerbosch(List R, List P, List X) implements the bronKer-bosch algorithm 
        to find cliques, outputs a list of lists containing the id of the nodes in each clique""" 
        
        if((len(P)==0) and (len(X) == 0)):
            self.cliques.append(R)
            return 
        for v in P.copy():
            RR = R[::]
            RR.append(v.idn)
            self.bronKerbosch(RR, self.intersection(P, self.N(v)), self.intersection(X, self.N(v)))
            P.remove(v)
           
            X.append(v)
           
    def intersection(self, lst1, lst2):
        lst3 = [value for value in lst1 if value in lst2]
        return lst3 
    
    def N(self, v):
        l = []
        for nei in v.neighbours:
            l.append(self.adjarr[nei])
        return l
    
    def isAdjacentn(self, nn1, nn2):
        n1 = self.adjarr[nn1]
        n2 = self.adjarr[nn2]
        len1 = len(n1.neighbours)
        len2 = len(n2.neighbours)
        if(len1<len2):
            for nei in n1.neighbours:
                if(nei == n2.idn):
                    return True 
            return False 
        else:
            for nei in n2.neighbours:
                if(nei == n1.idn):
                    return True 
            return False 
        
    
    
    
    def isAdjacentc(self, c1, c2):
        count = 0
        for a in c1:
            for b in c2:
                if(self.isAdjacentn(a,b) == True): #for 2-cliques
                #if(a == b):
                    count+=1
        return (count>1)
    
