import collections
import random

class AntColony:

    def __init__(self, cities):

        self.cities = cities
        print("ant colony init.")
        self.probabilityMap = self.cityDistanceProb()

        self.visited = set(); self.visited.add(-1)
        tour = self.createTour()

        




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

    
    def getNextCity(self, city):
        """getting the next city from the probability map"""

        # while next city not in visited already
        choice = -1
        
        while choice in self.visited:
            choice = random.choices(
                    population = self.probabilityMap[city],
                    weights = [i[1] for i in self.probabilityMap[city]]
                )[0][0]
        return choice
    

    def createTour(self):
        tour = [0]
        curCity = self.cities[0]

        while len(tour) <= len(self.cities):
            nextCity = self.getNextCity(curCity)
            tour.append(nextCity)

            curCity = self.cities[nextCity]
            # print("tour ->", tour)

            self.visited.add(nextCity)
        
        tour.append(0)
        print("tour ->", tour)
        return tour