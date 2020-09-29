from Map import Map
from A import aStar

import numpy as np
import matplotlib.pyplot as plt


### Varibles ########
mapSize = 500       #
nodeCount = 60      #
neighbourCount = 5  #
#####################


m = Map(mapSize)    # Create map object (mapSize X mapSize)
m.randomMap(nodeCount, neighbourCount) # Create random map of nodes

a = aStar(m)    # Run aStar on m



fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

path = np.array(a.path)
allPoints = np.array(m.allCoords)

ax.scatter(allPoints[:, 0], allPoints[:, 1], color = 'red')
ax.scatter(path[:, 0], path[:, 1])

ax.plot(path[:, 0], path[:, 1], color = 'green')

ax.set_xlabel("Time taken: " + str(a.timeTaken))
plt.show()


