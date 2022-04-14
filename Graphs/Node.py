##Note undirected graph is the goal here, so symmetry  in connection of neighbours is a necessity, 
## hence addNeighbour function dictates that if A is connected to B then B is connected to A


class Node: 
    def __init__(self, value, neighbours=None) -> None:
        self.value = value
        if neighbours == None:
            self.neighbours = []
        else:
            self.neighbours = neighbours;

    def addNeighbour(self, neighbour):
        self.neighbours.append(neighbour)
        neighbour.neighbours.append(self)
 

    def numberOfNeighbours(self): 
        return len(self.neighbours)
    
       
    def hasNeighbour(self):
        if self.numberOfNeighbours > 0: 
            return True
        return False