from random import randint as r
from random import choice
from math import sqrt


# Map object consisting of a set of Nodes
class Map():
    def __init__(self, gridSize):
        self.gridSize = gridSize
        
        self.startNode = None
        self.endNode = None
        self.nodeList = None


    # Node object
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
        
        
        # Updates gCost, hCost, and fCost
        def updateCosts(self, prevNode, endNode):
            self.gCost = sqrt(((prevNode.X - self.X) ** 2) + ((prevNode.Y - self.Y) ** 2))
            
            self.hCost = sqrt(((self.X - endNode.X) ** 2) + ((self.Y - endNode.Y) ** 2))
            
            self.fCost = self.gCost + self.hCost
            self.Parent = prevNode


    # Generates map with nodeCount nodes with maxNeighbours neighbours each
    def randomMap(self, nodeCount, maxNeighbours = 5):
        self.startNode = self.Node(r(10, self.gridSize - 10), r(10, self.gridSize - 10))    # Generate start node
        self.endNode   = self.Node(r(10, self.gridSize - 10), r(10, self.gridSize - 10))    # Generate end node
        
        self.nodeList  = [self.Node(r(10, self.gridSize - 10), r(10, self.gridSize) - 10) for i in range(0, nodeCount - 2)] # Generate remaining nodes and store in self.nodeList


        # Add neighbours to start and end nodes
        for i in range(0, maxNeighbours):
            startNeighbour = choice(self.nodeList)
            endNeighbour = choice(self.nodeList)
            
            self.startNode.Neighbours.add(startNeighbour)
            startNeighbour.Neighbours.add(self.startNode)
            
            self.endNode.Neighbours.add(endNeighbour)
            endNeighbour.Neighbours.add(self.endNode)
        
        # Add neighbours to remaining nodes
        for currentNode in self.nodeList:
            for i in range(0, maxNeighbours):
                neighbour = choice(self.nodeList)
                
                neighbour.Neighbours.add(currentNode)
                currentNode.Neighbours.add(neighbour)


    # Prints coordinates of each node on a newline clearly showing start and end
    def __str__(self):
        retStr = ""
        
        retStr += "Start: " + str(self.startNode.X) + ", " + str(self.endNode.Y) + "\n"
        
        for node in self.nodeList:
            retStr += str(node.X) + ", " + str(node.Y) + "\n"
            
        retStr += "End: " + str(self.endNode.X) + ", " + str(self.endNode.Y)
        
        return retStr


