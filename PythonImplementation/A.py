from math import sqrt
import time


class aStar():
    def __init__(self, mapObject):
        self.Map = mapObject    # Map object
        self.open, self.closed = [mapObject.startNode], []  # Open/Closed nodes
        self.path = []  # Shortest path through nodes
        
        self.startTime = time.time()    # Used to time the algorithm
        self.timeTaken = None           # Total time taken by the algorithm
        
        
        try:
            self.expand(mapObject.startNode)
        except:
            print("No route found.")
    
    
    # Opens or closes nodes, expands neighbours
    def expand(self, currentNode):
        if currentNode == self.Map.endNode: # If endNode reached
            self.timeTaken = str(time.time() - self.startTime)
            print("Route found in " + str(self.timeTaken))
            
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
            print(current.Coords)
            
            self.path.append(current.Coords)
            current = current.Parent

        return True


