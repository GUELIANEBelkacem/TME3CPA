from tme3 import *
from tm3grapheGen import *

g = FourClusterGraph(0.07, 0.0008)
cd = CommunityDetection(g.exportGraph())
# cd.labelPropagation()
cd.CPM()
print(cd.label)
print(set(cd.label))
g.drawGraph(cd.label)













































#cd.labelPropagation()
# cd.CPM()
# n1 = Node(1)
# P = []
# for i in range(cd.n):
#     P.append(cd.listy[i])
# cd.bronKerbosch([],P , [])

# print(cd.label)
# print(cd.cliques)
# # print(cd.listy)

# print(cd.isAdjacentc(cd.cliques[0], cd.cliques[1]))


# n1 = Node(1)
# n2 = Node(2)
# n1.nextn = n2
# print(n1.nextn == n2)
# print(cd.isAdjacentn(n1,n2))
# n3 = Node(3)
#n1.nextn.nextn = n3


# l1=[]
# l2=[]
# l1.append(n1)
# l1.append(n2)
# l2.append(n2)
# l2.append(n3)

# l3 = cd.intersection(l1,l2)

# print(cd.N(cd.listy[0]))