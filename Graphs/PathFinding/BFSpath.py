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
    print(node.value, node.numberOfNeighbours(), [x.value for x in node.neighbours])

    


#BFS algorithm

frontier = Queue()
reached = set()

frontier.put(nodeA)
reached.add(nodeA)

while not frontier.empty():
    current = frontier.get()
    for next in set(current.neighbours):
        if next not in reached:
            frontier.put(next)
            reached.add(next)





frontier = Queue()
came_from = dict()

frontier.put(nodeA)
came_from[nodeA] = None

while not frontier.empty():
    current = frontier.get()
    for next in set(current.neighbours):
        if next not in came_from:
            frontier.put(next)
            came_from[next] = current



print({k.value:v.value for (k,v) in came_from.items() if v != None})



def findPath(start, finish):
    finishFinal = finish
    path = []
    while finish != start:
        path.append(came_from[finish])
        finish = came_from[finish]
    
    
    return f"{'-'.join([x.value for x in path][::-1])}-{finishFinal.value}"


print(findPath(nodeA, nodeG))


