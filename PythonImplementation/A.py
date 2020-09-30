from math import sqrt
from pQueue import pQueue
import time


class aStar():
    def __init__(self, mapObject):
        self.Map = mapObject    # Map object
        self.priorityQueue = pQueue()   #Priority queue of nodes
        self.path = []  # Shortest path through nodes
        
        self.startTime = time.time()    # Used to time the algorithm
        self.timeTaken = None           # Total time taken by the algorithm
        
        
        self.expand(mapObject.startNode)
    
    
    # Opens or closes nodes, expands neighbours
    def expand(self, currentNode):
        if currentNode == self.Map.endNode: # If endNode reached
            self.timeTaken = str(time.time() - self.startTime)
            print("Route found in " + str(self.timeTaken))
            
            return self.showRoute(currentNode)
        
        
        currentNode.Open = 0
        
        # Update cost of neighbour nodes and add to priority queue if open
        for neighbour in currentNode.Neighbours:
            if neighbour.Open:
                neighbour.updateCosts(currentNode, self.Map.endNode)
                self.priorityQueue.insert(neighbour)
        
        return self.expand(self.priorityQueue.get())


    # Prints coordinates of items in a found route
    def showRoute(self, current):
        while current is not None:
            print(current.Coords)
            
            self.path.append(current.Coords)
            current = current.Parent

        return True


