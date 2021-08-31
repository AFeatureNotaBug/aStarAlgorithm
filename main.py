from Map import Map


### Varibles ####################
mapSize = 500      # In pixels  #
nodeCount = 50                  #
neighbourCount = 3              #
#################################


m = Map(mapSize)                        # Create map object of size mapSize * mapSize
m.randomMap(nodeCount, neighbourCount)  # Create random map of nodes

a = m.aStar()                           # Run aStar on m

m.showRoute()
