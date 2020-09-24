# aStarPython
Simple A* Algorithm written in Python. Works in both Python2.7 and Python3.6.

More utilities in order to create meaningful maps to come.


## Overview
Simple implementation of the A* algorithm. Each file is covered in more detail below, A.py contains the aStar class which, given a Map object (class in Map.py) consisting of Nodes (Class in Map.py), will determine the shortest route from the Map startNode to the Map endNode.

## A.py
This file contains the aStar algorithm which expects a map object to be provided of a certain format, given this map object it will determine the shortest route through the nodes of the map. The algorithm operates by maintaining a priority queue managed by the priorityQueue function, 'costs' of Nodes are determined in the Node class, and the queue gives priority to Nodes with lower 'cost'.

The algorithm also makes use of a function named "expand" which is responsible for:
* Opening new Nodes for consideration by the algorithm
* Closing Nodes that no longer require analysing
* Handling cost updates of Nodes

Nodes in the shortest route found are added to the self.path list in the showRoute function, which also displays a found route in the terminal.  

## Map.py
The Map class maintains a Map object which consists of a provided size and Node objects, the Node class is found within the Map class.

A Node consists of:
* X and Y coordinates
* gCost   - Distance from the Node to the previously analysed neighbour Node
* hCost   - Distance from the Node to the end Node
* fCost   - The sum of hCost and gCost
* Parent  - The previous node in the shortest route

Each Map object has clearly defined start and end nodes stored in self.startNode and self.endNode.

There is a function "randomMap(nodeCount, maxNeighbours)" which automatically generates a map of nodeCount nodes with maxNeighbours neighbours each. There is also a function used to display the Nodes in the Map in the terminal.

## main.py
This file is a simple test in order to run the program, alter the mapSize, nodeCount, and neighbourCount variables in order to generate different maps with different routes.
