from math import sqrt

class aStar():
    def __init__(self, mapObject):
        self.Map = mapObject    # Map object
        self.open, self.closed = [mapObject.startNode], []  # Open/Closed nodes
        self.path = []  # Shortest path through nodes
        
        try:
            self.expand(mapObject.startNode)
            
        except:
            print("No route found.")
    
    
    # Opens or closes nodes, expands neighbours
    def expand(self, currentNode):
        if currentNode == self.Map.endNode: # If endNode reached
            print("Route found.")
            return self.showRoute(currentNode)
        
        
        self.closed.append(currentNode)
        self.open.remove(currentNode)
        
        # Open and update costs of neighbour nodes
        for neighbour in currentNode.Neighbours:
            if neighbour not in self.closed:
                self.open.append(neighbour)
                neighbour.updateCosts(currentNode, self.Map.endNode)
        
        return self.priorityQueue()


    # Priority queue, lower fCost means higher priority
    def priorityQueue(self):
        lowest = None
        
        for openNode in self.open:
            if not lowest:
                lowest = openNode
                
            else:
                if openNode.fCost < lowest.fCost:
                    lowest = openNode
        
        return self.expand(lowest)
    
    
    # Prints coordinates of items in a found route
    def showRoute(self, current):
        while current is not None:
            print(current.X, current.Y)
            
            self.path.append(current)
            current = current.Parent

        return True


