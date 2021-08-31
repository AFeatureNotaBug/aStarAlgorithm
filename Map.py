from random import randint as r
from random import choice
from math import sqrt

import numpy as np
import pickle
import time

from pQueue import pQueue


# Map object consisting of a set of Nodes
class Map():
    def __init__(self, gridSize):
        """
         # gridSize  - Size of the map
         # startNode - Starting node in map traversal
         # endNode   - Ending node in map traversal
         # nodeList  - List of all Node objects in map
         # path      - List of all Node objects in shortest path
         # prioQ     - Priority queue used by aStar
        """
        self.gridSize = gridSize
        
        self.startNode = None
        self.endNode = None
        
        self.nodeList = []
        self.path = None
        
        self.prioQ = pQueue()


    # Node object
    class Node():
        def __init__(self, coordinates):
            """
             # Coords - X, Y(, Z) coordinates
             # Open   - Whether or not the node is open for visiting (Closed once assessed)
             # fCost  - gCost + hCost
                            - gCost = Distance to previous neighbour
                            - hCost = Distance to endNode 
             # Parent - Previous node in shortest route
            """
            self.Coords = coordinates   #numpy array
            self.Open = 1
            self.fCost = 0
            self.Parent = None
            self.Neighbours = set()
        
        
        # Updates gCost, hCost, and fCost
        def updateCosts(self, prevNode, endNode):
            gCost = np.linalg.norm(prevNode.Coords - self.Coords, 2)
            hCost = np.linalg.norm(self.Coords - endNode.Coords, 2)
            
            self.fCost = gCost + hCost
            self.Parent = prevNode


    def randomMap(self, nodeCount, maxNeighbours = 5):
        """Generates map with nodeCount nodes with maxNeighbours neighbours each"""
        self.startNode = self.Node(np.random.randint(10, self.gridSize - 10, (3)))
        self.startNode.Open = 0
        
        self.endNode = self.Node(np.random.randint(10, self.gridSize - 10, (3)))

        for i in range(0, nodeCount - 2):
            newNode = self.Node(np.random.randint(10, self.gridSize - 10, (3)))
            self.nodeList.append(newNode)
        
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


    def save(mapObj, filename):
        """Save map with given filename"""
        saveFile = open("Maps/" + filename + ".map", 'wb')
        pickle.dump(mapObj, saveFile, pickle.HIGHEST_PROTOCOL)
        saveFile.close()


    def load(filename):
        """Load map with given filename"""
        loadFile = open("Maps/" + filename, 'rb')
        mapObj = pickle.load(loadFile)
        loadFile.close()
        
        return mapObj


    def __str__(self):
        """Prints coordinates of each node on a newline clearly showing start and end"""
        retStr = ""
        
        retStr += "Start: " + str(self.startNode.Coords) + "\n"
        
        for node in self.nodeList:
            retStr += str(node.Coords) + "\n"
            
        retStr += "End: " + str(self.endNode.Coords)
        
        return retStr


    def aStar(self):
        """Manages execution of the aStar algorithm, see expand function"""
        self.prioQ.clear()         # Clear prio queue from previous usage
        startTime = time.time()    # Used to time the algorithm
        
        try:
            endTime = self.expand(self.startNode)
            print("Route found in " + str(endTime - startTime) + "\n")
            self.showRoute()
            
            return
            
        except:
            print("No route found")


    def expand(self, currentNode):
        """Opens/closes nodes, expands neighbours"""
        if currentNode == self.endNode: # If endNode reached
            endTime = time.time()
            p = []
            
            while currentNode is not None:
                p.append(currentNode.Coords)
                currentNode = currentNode.Parent
            
            self.path = np.array(p[::-1])
            
            return endTime
            
        else:
            # Update cost of neighbour nodes and add to priority queue if open
            for neighbour in currentNode.Neighbours:
                if neighbour.Open:
                    neighbour.Open = 0
                    neighbour.updateCosts(currentNode, self.endNode)
                    self.prioQ.insert(neighbour)
                    
            
            return self.expand(self.prioQ.get())


    def showRoute(self):
        """Print all Node objects in shortest path"""
        for coord in self.path:
            print(coord)
