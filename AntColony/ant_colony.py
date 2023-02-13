import time, os
from utils import getPathLength, getPathCoords
import matplotlib.pyplot as plt
import collections
import random

class AntColony:

    def __init__(self, cities):

        self.cities = cities
        self.feromonePresence = 100
        iterations = 10000

        self.feromoneMatrix = [[1000 for j in range(len(self.cities))] for i in range(len(self.cities))]

        for i in range(iterations):
            path, pathLength = self.getRandomPath()
            self.updateFeromoneMatrix(path, pathLength)

        self.showFeromones()

    

    def getRandomPath(self):
        path = [0] * (len(self.cities) + 1)

        visited = 1

        while visited < len(self.cities):

            nextCity = 0
            while nextCity in path:
                nextCity = random.randint(0, len(self.cities) - 1)

            path[visited] = nextCity
            visited += 1

        return path, getPathLength(path, self.cities)

    
    def updateFeromoneMatrix(self, path, pathLength):
        # print(path, pathLength)

        for r in range(1, len(path)):
            l = r - 1
            # print(path[l], path[r])
            self.feromoneMatrix[ path[l] ][ path[r] ] += (self.feromonePresence / pathLength)
            self.feromoneMatrix[ path[r] ][ path[l] ] += (self.feromonePresence / pathLength)

    
    def showFeromones(self):
        print()
        for r in range(len(self.feromoneMatrix)):
            for c in range(len(self.feromoneMatrix[0])):
                print(self.feromoneMatrix[r][c], end=' - ')
            print()