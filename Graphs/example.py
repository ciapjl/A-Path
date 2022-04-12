from Graph import *
from Node import *


node1 = Node(1)
node2 = Node(2)

node1.addNeighbour(node2)

node3 = Node(3, [node2,node1])



graph1 = Graph([node1,node2, node3])

print(graph1.areConnected(node1,node3))
