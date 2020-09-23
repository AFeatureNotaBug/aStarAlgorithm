from Map import Map
from A import aStar

import py as py


m = Map(500)    # Create map object (500x500)
m.randomMap(60) # Create a random map of 60 nodes

a = aStar(m)    # Run aStar on m


"""Draws the map of nodes with route"""
window = py.display.set_mode((500, 500))
py.display.flip()


main = True
while main:
    for event in py.event.get():
        if event.type == py.QUIT:
            main = False

    # Draw each Node as a white square
    for item in m.nodeList:
        py.draw.rect(window, (255, 255, 255), [item.X, item.Y, 6, 6])

    # Draw each Node in path as blue square, purple lines between path Nodes
    curr = m.endNode
    while curr.Parent:
        par = curr.Parent
        
        py.draw.rect(window, (0, 0, 255), [curr.X, curr.Y, 6, 6])
        py.draw.line(window, (200, 10, 200), (curr.X, curr.Y), (par.X, par.Y))
        curr = curr.Parent

    # Draw start and end nodes
    py.draw.rect(window, (255, 0, 0), [m.startNode.X, m.startNode.Y, 6, 6])
    py.draw.rect(window, (0, 255, 0), [m.endNode.X, m.endNode.Y, 6, 6])

    py.display.update()
