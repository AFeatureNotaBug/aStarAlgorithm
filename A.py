from math import sqrt

class aStar():
    def __init__(self, mapObject):
        self.Map = mapObject
        self.open, self.closed = [mapObject.startNode], []
        
        try:
            self.expand(mapObject.startNode)
            
        except:
            print("No route found.")
    
    
    # Opens/Closes nodes, expands neighbours
    def expand(self, currentNode):
        if currentNode == self.Map.endNode:
            print("Route found.")
            print(self.Map.endNode.Parent)
            return self.showRoute(currentNode)
            
        self.closed.append(currentNode)
        self.open.remove(currentNode)
        
        for neighbour in currentNode.Neighbours:
            if neighbour not in self.closed:
                self.open.append(neighbour)
                
                self.updateCosts(currentNode, neighbour)
        
        
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
    
    
    def updateCosts(self, current, neighbour):
        neighbour.gCost = sqrt(((current.X - neighbour.X) ** 2) + ((current.Y - neighbour.Y) ** 2))
        neighbour.hCost = sqrt(((neighbour.X - self.Map.endNode.X) ** 2) + ((neighbour.Y - self.Map.endNode.Y) ** 2))
        neighbour.fCost = neighbour.gCost + neighbour.hCost
        neighbour.Parent = current


    def showRoute(self, current):
        while current is not None:
            print(current)
            current = current.parent

        return True

