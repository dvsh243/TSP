import time, os
from utils import getPathLength, getPathCoords
import matplotlib.pyplot as plt
import collections
import random

class AntColony:

    def __init__(self, cities):

        self.cities = cities
        self.feromonePresence = 100   # 100
        iterations = 150000

        self.probabilityMap = self.cityDistanceProb()
        self.feromoneMatrix = [[1000 for j in range(len(self.cities))] for i in range(len(self.cities))]

        # self.showFeromones()

        for i in range(iterations):
            self.visited = set(); self.visited.add(0)
            self.tour = self.createTour()
            self.updateFeromoneMatrix(self.tour, getPathLength(self.tour, self.cities))

            # print(f"{i} tour ->", tour, getPathLength(tour, self.cities))

            if i % 2000 == 0:
                print(f"{(i / iterations) * 100} % done.", end='\r')
                # self.showFeromones(); print()
                # print(i)
                # self.showVisual()

        
        # self.showFeromones()

        


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

    def showFeromones(self):
        os.system('cls')
        for r in range(len(self.feromoneMatrix)):
            for c in range(len(self.feromoneMatrix)):
                print(self.feromoneMatrix[r][c], end=' - ')
            print()

        
    def getMaxFeromonePath(self):
        nextCityMatrix = [[] for _ in range(len(self.cities))]

        for r in range(len(self.feromoneMatrix)):
            possibleNext = []
            for c, fer in enumerate(self.feromoneMatrix[r]):
                possibleNext.append( [fer, c] )
            possibleNext.sort(key = lambda i: i[0], reverse = True)  # sorting by highest feromones firts
            # print(f"City ({r}) --> {possibleNext}")

            nextCityMatrix[r] = possibleNext

        # print()        
        # for r in range(len(nextCityMatrix)):
        #     for c in range(len(nextCityMatrix[0])):
        #         print(nextCityMatrix[r][c], end=' - ')
        #     print()
        
        # # getting the first edge by getting highest feromone path between 2 cities
        # visited = collections.defaultdict(int)  # all cities can get maximum 2 edges
        # print()
        # for c in range(len(nextCityMatrix[0])):
        #     nextCity, maxFer = None, 0
        #     for r in range(len(nextCityMatrix)):
        #         if nextCityMatrix[c][r][0] > maxFer and visited[nextCityMatrix[c][r][1]] < 2:
        #             maxFer = nextCityMatrix[c][r][0]
        #             nextCity = nextCityMatrix[c][r][1]
        #     print(f"({c}) -> ({nextCity})")
        #     visited[nextCity] += 1
        # print(visited)

    def showVisual(self):
        xpath, ypath = getPathCoords(self.tour, self.cities)
        plt.scatter(xpath, ypath)
        plt.suptitle(f" Ant Colony - {getPathLength(self.tour, self.cities)} km")
        plt.plot(xpath, ypath)
        plt.pause(0.01)
        plt.clf()