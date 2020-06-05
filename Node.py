class Node():
    def __init__(self, gridSize):
        self.X, self.Y = randint(10, gridSize - 10, randint(10, gridSize - 10)
        self.gCost, self.hCost, self.fCost = 0, 0, 0
        self.parentNode = None
        self.Neighbours = []
