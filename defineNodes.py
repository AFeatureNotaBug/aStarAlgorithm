#Given a list of nodes, the function will refine into a list of only possible paths
from NodeCreation import Node
from math import sqrt
from A import aStar

def sort_nodes(startNode, endNode, nodeDetails):

    allNodes = [Node(node[0], node[1], node[2], node[3::]) for node in nodeDetails] #Create list of all nodes with unsorted neighbours


   #Define start and end nodes given by input
    for node in allNodes:
        if node.name == startNode:
            startNode = node

        elif node.name == endNode:
            endNode = node

    #Sort node neighbours into lists of nodes
    for messyNode in allNodes:
        newNeighbours = []
        messyNodeNeighbours = messyNode.NeighbourNodes

        for neighbour in messyNodeNeighbours:
            for node in allNodes:
                if node.name == neighbour:
                    newNeighbours.append(node)


        messyNode.NeighbourNodes = newNeighbours

    #Remove start and end nodes from list of all nodes
    allNodes.remove(startNode)
    allNodes.remove(endNode)


    #Remove all nodes with only one neighbour
    for node in allNodes:
        if len(node.NeighbourNodes) <= 1:
            allNodes.remove(node)

    return startNode, endNode, allNodes

"""
startNode = "1"
endNode = "8"

nodeDetails = [[1, 100, 100, 2, 3],
               [2, 200, 50, 1, 5],
               [3, 200, 150, 1, 4],
               [4, 230, 100, 3, 5],
               [5, 300, 90, 2, 4, 6, 7],
               [6, 350, 78, 5, 7],
               [7, 350, 123, 5, 6, 8, 9],
               [8, 390, 180, 7],
               [9, 219, 170, 7, 10],
              [10, 210, 175, 9]]


startNode, endNode, allNodes = sort_nodes(startNode, endNode, nodeDetails)

path = aStar(startNode, endNode)
"""
