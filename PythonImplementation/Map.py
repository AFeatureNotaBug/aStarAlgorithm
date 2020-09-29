from random import randint as r
from random import choice
from math import sqrt
import numpy as np


# Map object consisting of a set of Nodes
class Map():
    def __init__(self, gridSize):
        self.gridSize = gridSize
        
        self.startNode = None
        self.endNode = None
        
        self.nodeList = []
        self.allCoords = []


    # Node object
    class Node():
        def __init__(self, coordinates):
            """
             # X, Y   - X and Y coordinates
             # gCost  - Distance to previous neighbour
             # hCost  - Distance to endNode
             # fCost  - gCost + hCost
             # Parent - Previous node in shortest route
            """
            self.Coords = coordinates   #numpy array
            self.gCost, self.hCost, self.fCost = 0, 0, 0
            
            self.Parent = None
            self.Neighbours = set()
        
        
        # Updates gCost, hCost, and fCost
        def updateCosts(self, prevNode, endNode):
            self.gCost = sqrt(np.sum((prevNode.Coords - self.Coords) ** 2))
            self.hCost = sqrt(np.sum((self.Coords - endNode.Coords) ** 2))
            self.fCost = self.gCost + self.hCost
            
            self.Parent = prevNode


    # Generates map with nodeCount nodes with maxNeighbours neighbours each
    def randomMap(self, nodeCount, maxNeighbours = 5):
        self.startNode = self.Node(np.array([r(10, self.gridSize - 10), r(10, self.gridSize - 10)]))    # Generate start node
        self.endNode   = self.Node(np.array([r(10, self.gridSize - 10), r(10, self.gridSize - 10)]))    # Generate end node

        for i in range(0, nodeCount - 2):
            newPoint = self.Node(np.array([r(10, self.gridSize - 10), r(10, self.gridSize - 10)]))
            
            self.nodeList.append(newPoint)
            self.allCoords.append(newPoint.Coords)
        
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


