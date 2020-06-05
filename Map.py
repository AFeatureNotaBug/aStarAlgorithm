from random import randint as r
from random import choice


class Map():
    def __init__(self, gridSize):
        self.gridSize = gridSize
        
        self.startNode = None
        self.endNode = None
        self.nodeList = None


    class Node():
        def __init__(self, x, y):
            """
             # X, Y   - X and Y coordinates
             # gCost  - Distance to previous neighbour
             # hCost  - Distance to endNode
             # fCost  - gCost + hCost
             # Parent - Previous node in shortest route
            """
            self.X, self.Y = x, y
            self.gCost, self.hCost, self.fCost = 0, 0, 0
            
            self.Parent = None
            self.Neighbours = set()


    def randomMap(self, nodeCount, maxNeighbours = 5):
        self.startNode = self.Node(r(10, self.gridSize - 10), r(10, self.gridSize - 10))
        self.endNode   = self.Node(r(10, self.gridSize - 10), r(10, self.gridSize - 10))
        self.nodeList  = [self.Node(r(10, self.gridSize - 10), r(10, self.gridSize) - 10) for i in range(0, nodeCount - 2)]

        for i in range(0, maxNeighbours):
            startNeighbour = choice(self.nodeList)
            endNeighbour = choice(self.nodeList)
            
            self.startNode.Neighbours.add(startNeighbour)
            startNeighbour.Neighbours.add(self.startNode)
            
            self.endNode.Neighbours.add(endNeighbour)
            endNeighbour.Neighbours.add(self.endNode)
            
        for current in self.nodeList:
            for i in range(0, maxNeighbours):
                neighbour = choice(self.nodeList)
                
                neighbour.Neighbours.add(current)
                current.Neighbours.add(neighbour)


    def __str__(self):
        retStr = ""
        
        retStr += "Start: " + str(self.startNode.X) + ", " + str(self.endNode.Y) + "\n"
        
        for node in self.nodeList:
            retStr += str(node.X) + ", " + str(node.Y) + "\n"
            
        retStr += "End: " + str(self.endNode.X) + ", " + str(self.endNode.Y)
        
        return retStr


