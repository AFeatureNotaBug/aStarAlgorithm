from Map import Map
from A import aStar

import numpy as np
import matplotlib.pyplot as plt


### Varibles ########
mapSize = 500       #
nodeCount = 50      #
neighbourCount = 3  #
#####################


m = Map(mapSize)                        # Create map object (mapSize X mapSize)
m.randomMap(nodeCount, neighbourCount)  # Create random map of nodes

a = aStar(m)                            # Run aStar on m


fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

path = np.array(a.path)
uncheckedP = np.array([node.Coords for node in m.nodeList if node.Open])
checkedP = np.array([node.Coords for node in m.nodeList if not node.Open])

ax.scatter(uncheckedP[:, 0], uncheckedP[:, 1], uncheckedP[:, 2], color = 'red')
ax.scatter(checkedP[:, 0], checkedP[:, 1], checkedP[:, 2], color = 'green')

ax.scatter(path[:, 0], path[:, 1], path[:, 2], color = 'green')
ax.plot(path[:, 0], path[:, 1], path[:, 2], color = 'blue')

ax.set_xlabel("Time taken: " + str(a.timeTaken))
plt.show()


