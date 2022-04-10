

#TODO: define Graph class using 

class Node: 
    def __init__(self, value, neighbours=None) -> None:
        self.value = value
        if neighbours == None:
            self.neighbours = []
        else:
            self.neighbours = neighbours;

    def addNeighbour(self, neighbour):
        self.neighbours.append(neighbour)

    

class Graph: 
    def __init__(self, nodes=None) -> None:
        ##initialize empty 
        if nodes is None:
            self.nodes = []
        else:
            self.nodes = nodes
        

    def addNode(self, node):
        self.nodes.append(Node)