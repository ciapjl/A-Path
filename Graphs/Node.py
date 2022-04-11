
class Node: 
    def __init__(self, value, neighbours=None) -> None:
        self.value = value
        if neighbours == None:
            self.neighbours = []
        else:
            self.neighbours = neighbours;

    def addNeighbour(self, neighbour):
        self.neighbours.append(neighbour)
 

    def numberOfNeighbours(self): 
        return len(self.nodes)
    
       
    def hasNeighbour(self):
        if self.numberOfNeighbours > 0: 
            return True
        return False