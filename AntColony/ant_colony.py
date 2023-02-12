import collections
import random

class AntColony:

    def __init__(self, cities):

        self.cities = cities
        print("ant colony init.")
        self.probabilityMap = self.cityDistanceProb()

        # self.getNextCity(self.cities[0])


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
            
            # choosing a random city from a weighted population
            # choice = random.choices(
            #     population = distMap[city],
            #     weights = [i[1] for i in distMap[city]]
            # )
            # print("city chosen ->", choice)
            
        return distMap

    
    def getNextCity(self, city):
        """getting the next city from the probability map"""
        choice = random.choices(
                population = self.probabilityMap[city],
                weights = [i[1] for i in self.probabilityMap[city]]
            )
        return choice[0]