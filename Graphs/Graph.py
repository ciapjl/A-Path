from Node import *


    

class Graph: 
    def __init__(self, nodes=None) -> None:
        ##initialize empty 
        if nodes is None:
            self.nodes = []
        else:
            self.nodes = nodes
    
    def addNode(self, node):
        self.nodes.append(node)

    def findNode(self, value):
        for node in self.nodes: 
            if node.value == value:
                return True
        return None

    def addEdge(self, value1, value2):
        node1 = self.findNode(value1)
        node2 = self.findNode(value2)

        if node1 != None and node2!= None:
            node1.addNeighbour(node2)
            node2.addNeighbour(node1)
        else:
            raise ValueError(f'No pair of Nodes with values {value1} and {value2} were found')
        



    def areConnected(self, node1, node2):
        if node1 in node2.neighbours or node2 in node1.neighbours:
            return True
        return False

        

  
    