import time
from utils import getPathLength, getPathCoords
import matplotlib.pyplot as plt
import collections
import random

class AntColony:

    def __init__(self, cities):

        self.cities = cities
        self.feromonePresence = 10
        print("ant colony init.")
        self.probabilityMap = self.cityDistanceProb()
        self.feromoneMatrix = [[10 for j in range(len(self.cities))] for i in range(len(self.cities))]


        for i in range(10000):
            self.visited = set(); self.visited.add(0)
            tour = self.createTour()
            self.updateFeromoneMatrix(tour, getPathLength(tour, self.cities))

            # print(f"{i} tour ->", tour, getPathLength(tour, self.cities))
            

        print()
        


    def cityDistanceProb(self):
        distMap = collections.defaultdict(list)  # city -> [list of distances from other cities] 
        
        for i in range(len(self.cities)):
            for j in range(len(self.cities)):
                if i == j: continue
                city1, city2 = self.cities[i], self.cities[j]

                distMap[city1].append( [j, city1.distance(city2)] )
                # print(f"{(city1.x, city1.y)} - {(city2.x, city2.y)} ----> {city1.distance(city2)}")
        
        
        # current distMap contains, city -> [list of distances from other cities (except itself)]
        # convert them into probabilities from 0 to 100
        for city in distMap:
            # print( (city.x, city.y) )
            minDist, maxDist = 10 ** 9, 0
            distSum = 0

            for dist in distMap[city]:
                minDist = min(minDist, dist[1])
                maxDist = max(maxDist, dist[1])
                distSum += dist[1]
            
            # calculated the maximum and the minimum
            # now normalizing the array values to sum upto 1000
            for dist in distMap[city]:
                dist[1] = (dist[1] / distSum)
            
        return distMap

    
    def getNextCity(self, cityIdx):
        """getting the next city from the probability map"""
        
        city = self.cities[cityIdx]
        
        weightList = [i[1] for i in self.probabilityMap[city]]

        # multiplying current weights with feromone matrix
        for i in range(len(weightList)):
            weightList[i] = weightList[i] * self.feromoneMatrix[cityIdx][i]

        # print(f"weight list for {(city.x, city.y)} -> ")
        # print(weightList)

        # while next city not in visited already
        choice = 0  # 0 is always in visited by default
        while choice in self.visited:

            choice = random.choices(
                    population = self.probabilityMap[city],
                    weights = weightList
                )[0][0]

        return choice
    

    def createTour(self):
        tour = [0]
        curCity = 0

        while len(tour) < len(self.cities):
            nextCity = self.getNextCity( curCity )
            tour.append(nextCity)

            curCity = nextCity

            self.visited.add(nextCity)
        
        tour.append(0)  # connect back to 0
        return tour
    

    def updateFeromoneMatrix(self, tour, tourLength):
        # also called reward matrix

        for j in range(1, len(tour) - 1):  # not taking the last edge because its just connecting back to 0
            i = j - 1
            c1, c2 = tour[i], tour[j]

            # inverse of tour length -> better tour length, higher the inverse, higher the probability of this edge being selected 
            self.feromoneMatrix[c1][c2] += (self.feromonePresence / tourLength)
            self.feromoneMatrix[c2][c1] += (self.feromonePresence / tourLength)

        # for r in range(len(self.feromoneMatrix)):
        #     for c in range(len(self.feromoneMatrix)):
        #         print(self.feromoneMatrix[r][c], end=' - ')
        #     print()

    def showVisual(self, path):
        xpath, ypath = getPathCoords(path, self.cities)
        plt.scatter(xpath, ypath)
        plt.suptitle(f" Ant Colony - {getPathLength(path, self.cities)} km")
        plt.plot(xpath, ypath)
        plt.pause(0.01)
        plt.clf()