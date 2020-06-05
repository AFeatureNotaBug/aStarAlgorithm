class Node():
    def __init__(self, name, x, y, neighbours):
        self.name = str(name)
        self.X, self.Y = int(x), int(y)
        self.gCost, self.hCost, self.fCost = 0, 0, 0
        self.parentNode = self
        self.NeighbourNodes = [str(item) for item in neighbours]
