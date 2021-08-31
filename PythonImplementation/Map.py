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


    # Node object
    class Node():
        def __init__(self, coordinates):
            """
             # Coords - X, Y(, Z) coordinates
             # Open   - Whether or not the node is open for visiting (Closed once assessed)
             # fCost  - gCost + hCost
                            + gCost = Distance to previous neighbour
                            + hCost = Distance to endNode 
             # Parent - Previous node in shortest route
            """
            self.Coords = coordinates   #numpy array
            self.Open = 1
            self.fCost = 0
            self.Parent = None
            self.Neighbours = set()
        
        
        # Updates gCost, hCost, and fCost
        def updateCosts(self, prevNode, endNode):
            gCost = sqrt(np.sum((prevNode.Coords - self.Coords) ** 2))
            hCost = sqrt(np.sum((self.Coords - endNode.Coords) ** 2))
            
            self.fCost = gCost + hCost
            self.Parent = prevNode


    """Generates map with nodeCount nodes with maxNeighbours neighbours each"""
    def randomMap(self, nodeCount, maxNeighbours = 5):
        self.startNode = self.Node(np.random.randint(10, self.gridSize - 10, (3)))
        self.startNode.Open = 0
        
        self.endNode = self.Node(np.random.randint(10, self.gridSize - 10, (3)))

        for i in range(0, nodeCount - 2):
            newPoint = self.Node(np.random.randint(10, self.gridSize - 10, (3)))
            
            self.nodeList.append(newPoint)
        
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
        
        retStr += "Start: " + str(self.startNode.Coords) + "\n"
        
        for node in self.nodeList:
            retStr += str(node.Coords) + "\n"
            
        retStr += "End: " + str(self.endNode.Coords)
        
        return retStr


