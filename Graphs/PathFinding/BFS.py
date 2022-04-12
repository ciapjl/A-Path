import sys

sys.path.insert(0,'/home/jean-luc/Documents/OdinProject/Portfolio/A-Path/Graphs')

from queue import Queue
from Graph import *
from Node import *


nodeA = Node('A')
nodeB = Node('B')
nodeC = Node('C')
nodeD = Node('D')
nodeE = Node('E')
nodeF = Node('F')
nodeG = Node('G')
nodeH = Node('H')
nodeI = Node('I')
nodeJ = Node('J')
nodeK = Node('K')

nodeA.addNeighbour(nodeB)
nodeB.addNeighbour(nodeC)
nodeB.addNeighbour(nodeD)
nodeC.addNeighbour(nodeG)
nodeC.addNeighbour(nodeH)
nodeD.addNeighbour(nodeE)
nodeD.addNeighbour(nodeF)
nodeH.addNeighbour(nodeI)
nodeE.addNeighbour(nodeI)
nodeI.addNeighbour(nodeJ)
nodeI.addNeighbour(nodeK)

graph = Graph(nodes=[nodeA,
nodeB,
nodeC,
nodeD,
nodeE,
nodeF,
nodeG,
nodeH,
nodeI,
nodeJ,
nodeK])

for node in graph.nodes:
    print(node.value, node.numberOfNeighbours(), node.neighbours)

    


#BFS algorithm

frontier = Queue()
reached = set()

frontier.put(nodeA)
reached.add(nodeA)

while not frontier.empty():
    current = frontier.get()
    for next in set(current.neighbours).difference(reached) :
        frontier.put(next)
        reached.add(next)
        print(next.value)






