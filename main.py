from defineNodes import sort_nodes
from random import randint
from A import aStar
import pygame, time, sys

start = time.time()

try:
    path = aStar(startNode, endNode)

    print("Time taken: " + str(time.time() - start))
    print("Route of " + str(len(path)) + " items found.")

except:
    print("No possible routes found.")
    sys.exit(0)


ask = str(raw_input("Enter y to draw, n to quit: ")).lower()

if ask == "y":
    window = pygame.display.set_mode((500, 500))
    pygame.display.flip()


    main = True
    while main:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False

        for item in allNodes:
            pygame.draw.rect(window, (255, 255, 255), [item.X, item.Y, 6, 6])

        for item in path:
            pygame.draw.rect(window, (0, 0, 255), [item.X, item.Y, 6, 6])
            pygame.draw.line(window, (200, 10, 200), (item.X, item.Y), (item.parentNode.X, item.parentNode.Y))

        pygame.draw.rect(window, (255, 0, 0), [startNode.X, startNode.Y, 6, 6])
        pygame.draw.rect(window, (0, 255, 0), [endNode.X, endNode.Y, 6, 6])

        pygame.display.update()
