#Given a list of nodes, the function will refine into a list of only possible paths
from NodeCreation import Node
from math import sqrt

def aStar(startNode, endNode):
    return expand(startNode, endNode, [startNode])


def priority_queue(endNode, openNodes, closed):
    #Function for queueing, lower cost means higher priority
    lowest = False

    for openNode in openNodes:
        if lowest:
            if openNode.fCost < lowest.fCost:
                lowest = openNode
        else:
            lowest = openNode

    return expand(lowest, endNode, openNodes, closed)


def expand(currentNode, endNode, openNodes, closed = []):
    print("Current: " + currentNode.name)

    #Function for expanding currently open nodes using the priority queue
    if currentNode == endNode:
        print("\nRoute found.")
        return sort_path(endNode)

    closed.append(currentNode) #Close previous node
    openNodes.remove(currentNode)

    for neighbourNode in currentNode.NeighbourNodes: 	#Iterate neighbouring nodes
        if neighbourNode not in closed:			#Check if a neighbour is closed
            openNodes.append(neighbourNode)			#Open neighbouring nodes and below calculate their costs
            neighbourNode.gCost = sqrt( ((currentNode.X - neighbourNode.X) ** 2) + ((currentNode.Y - neighbourNode.Y) ** 2) )
            neighbourNode.hCost = sqrt(((neighbourNode.X - endNode.X) ** 2) + ((neighbourNode.Y - endNode.Y) ** 2))
            neighbourNode.fCost = neighbourNode.gCost + neighbourNode.hCost
            neighbourNode.parentNode = currentNode	#Give the newly opened nodes a parent

    return priority_queue(endNode, openNodes, closed)


def sort_path(node, path = []):
    path.append(node)

    if node.parentNode == node:
        return [item for item in reversed(path)]

    return sort_path(node.parentNode, path = path)
