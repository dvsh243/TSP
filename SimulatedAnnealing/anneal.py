import random
from utils import getPathLength, getPathCoords
import matplotlib.pyplot as plt

class SimAnneal:
    
    def __init__(self, cities, optPath, decay = 0.995, visual = False):
        self.cities = cities

        self.temperature = 100
        self.max_temperature = 100
        self.stopping_temperature = 1
        self.decay = decay

        self.path = optPath
        self.minPath = None

        self.anneal(visual = visual)
    


    def anneal(self, visual = False):
        good, bad = 0, 0

        minTour = float('inf')
        
        i = 0
        while self.temperature > self.stopping_temperature:
            
            if i%100 == 0: print(f"minTour = {minTour}\ttemp = {self.temperature}", end='\r')

            i += 1
            self.temperature = self.temperature * self.decay

            newPath = self.twoCitiesSwap()
            
            if self.isPathBetter(newPath, self.path):
                if visual: self.showVisual()
                good += 1
                # if this newPath is better than the previous path we had we accept
                self.path = newPath

                if minTour > getPathLength(self.path, self.cities):
                    minTour = getPathLength(self.path, self.cities)
                    self.minPath = self.path


            elif self.acceptProbability():
                if visual: self.showVisual()
                bad += 1
                # this newPath is worse than the previous path
                # should we accept this worse path? based on the temperature
                self.path = newPath
        
        print(f"annealing loop ran total {i} times.")
        print("minTour -- > ", minTour)


    def isPathBetter(self, path1, path2):
        # if path 1 is better than path 2
        if getPathLength(path1, self.cities) < getPathLength(path2, self.cities):
            return True
        return False


    def acceptProbability(self):
        if random.randint(self.stopping_temperature, self.max_temperature) < self.temperature:
            return True
        return False


    def twoCitiesSwap(self):
        newPath = self.path.copy()
        u, v = random.randint(1, len(self.cities)-1), random.randint(1, len(self.cities)-1)
        while u == v:
            v = random.randint(1, len(self.cities)-1)
    
        # print(f"two cities to swap -- ({path[u]}) <-> ({path[v]})")
        newPath[v], newPath[u] = self.path[u], self.path[v]

        return newPath


    def threeCitiesSwap(self):
        newPath = self.path.copy()
    
        u = random.randint(1, len(self.cities)-1)
        v = random.randint(1, len(self.cities)-1)
        w = random.randint(1, len(self.cities)-1)
        while u == v:
            v = random.randint(1, len(self.cities)-1)
        while w == u or w == v:
            w = random.randint(1, len(self.cities)-1)
    
        # print(f"two cities to swap -- ({path[u]}) <-> ({path[v]})")
        newPath[v], newPath[u], newPath[w] = self.path[u], self.path[w], self.path[v]
        # v -> u, u -> w, w -> v

        return newPath

    
    def showVisual(self):
        xpath, ypath = getPathCoords(self.path, self.cities)
        plt.scatter(xpath, ypath)
        plt.suptitle(f" SimAnneal - {getPathLength(self.path, self.cities)} km")
        plt.plot(xpath, ypath)
        plt.pause(0.01)
        plt.clf()
