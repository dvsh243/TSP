import random
from utils import getPathLength


class SimAnneal:
    
    def __init__(self, cities, optPath, decay = 0.98):
        self.cities = cities

        self.temperature = 1000
        self.max_temperature = 1000
        self.stopping_temperature = 1
        self.decay = decay

        self.path = optPath

        self.anneal()
    


    def anneal(self):

        i = 0
        while self.temperature > self.stopping_temperature:
            if i % 50 == 0: print(f"acceptance probability -> {str((self.temperature / self.max_temperature) * 100)[:8]}%", end='\r')
            i += 1
            self.temperature = self.temperature * self.decay

            newPath = self.twoCitiesSwap()
            
            if self.isPathBetter(newPath, self.path):
                # if this newPath is better than the previous path we had we accept
                self.path = newPath

            elif self.acceptProbability():
                # this newPath is worse than the previous path
                # should we accept this worse path? based on the temperature
                self.path = newPath
        
        # print(f"New path -> {path} -> {getPathLength(self.path, self.cities)}")
        print(f"annealing loop ran total {i} times.")


    def isPathBetter(self, path1, path2):
        if getPathLength(path1, self.cities) < getPathLength(path2, self.cities):
            return True
        return False


    def acceptProbability(self):
        if random.randint(1, self.max_temperature) < self.temperature:
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