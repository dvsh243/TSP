import time

from utils import generateCities, visualizePath, getPathCoords, getPathLength
from BruteForce.brute_force import bruteForce
from BruteForce.brute_force_worst import bruteForceWorst
from NearestNeighbour.nearest_neighbour import nearestNeighbour
from Random.random_route import getRandomPath
from Swapping.two_opt import twoOptSwap
from Swapping.three_opt import threeOptSwap



class TSP:

    def __init__(self):

        self.VISUALIZE = True
        self.CITY_COUNT = 25  # (for 3 opt swap) 3 > N < 9 (for brute force)

        # - # - # - # - # - # - # - # - # - # - 
        self.BRUTE_FORCE = True
        self.RANDOM_PATH = True
        self.NEAREST_NEIGHBOUR = True
        
        self.SWAP_COUNT = 20000
        self.TWO_OPT = True
        self.THREE_OPT = True
        # - # - # - # - # - # - # - # - # - # - 

        self.cities = generateCities(self.CITY_COUNT)

        # randomPath = self.randomPathTSP()
        NNPath = self.nearestNeighbourTSP()
        # brutePath = self.bruteForceTSP()
        twoOptPath = self.twoOptTSP(NNPath)
        threeOptSwap = self.threeOptTSP(twoOptPath)

        if self.VISUALIZE: input("Enter any key to exit: ")


    def randomPathTSP(self):
        if not self.RANDOM_PATH: return None

        print(f"\n ---- RANDOM PATH ---- ")
        randomPath = getRandomPath(self.cities)
        tourLength = getPathLength(randomPath, self.cities)
        xpath, ypath = getPathCoords(randomPath, self.cities)
        if self.VISUALIZE: visualizePath(f"Random Path - {str(tourLength)[:8]} km", self.cities, xpath, ypath)
        print(f"Path followed -> {randomPath}\nTour Length -> {tourLength}")
        return randomPath
    

    def nearestNeighbourTSP(self):
        if not self.NEAREST_NEIGHBOUR: return None
    
        print(f"\n ---- NEAREST NEIGHBOUR ---- ")
        NNPath = nearestNeighbour(self.cities)
        tourLength = getPathLength(NNPath, self.cities)
        xpath, ypath = getPathCoords(NNPath, self.cities)
        if self.VISUALIZE: visualizePath(f"Nearest Neighbour - {str(tourLength)[:8]} km", self.cities, xpath, ypath)
        print(f"Path followed -> {NNPath}\nTour Length -> {tourLength}")
        return NNPath
    

    def twoOptTSP(self, OptPath: list):
        if not self.TWO_OPT: return None
    
        print(f"\n ---- 2 OPT SWAP ---- ")
        minTour, twoOptPath = twoOptSwap(OptPath, self.cities, N=self.SWAP_COUNT)
        xpath, ypath = getPathCoords(twoOptPath, self.cities)
        if self.VISUALIZE: visualizePath(f"2 Opt Swap - {str(minTour)[:8]} km", self.cities, xpath, ypath)
        print(f"Path followed -> {twoOptPath}\nTour Length -> {minTour}")
        return twoOptPath

    
    def threeOptTSP(self, OptPath: list):
        if not self.TWO_OPT: return None
        
        print(f"\n ---- 3 OPT SWAP ---- ")
        minTour, threeOptPath = threeOptSwap(OptPath, self.cities, N=self.SWAP_COUNT)
        xpath, ypath = getPathCoords(threeOptPath, self.cities)
        if self.VISUALIZE: visualizePath(f"3 Opt Swap - {str(minTour)[:8]} km", self.cities, xpath, ypath)
        print(f"Path followed -> {threeOptPath}\nTour Length -> {minTour}")
        return threeOptPath


    def bruteForceTSP(self):
        if not self.BRUTE_FORCE: return None

        print(f"\n ---- BRUTE FORCE ---- ")
        minTour, brutePath = bruteForce(self.cities)
        xpath, ypath = getPathCoords(brutePath, self.cities)
        if self.VISUALIZE: visualizePath(f"Brute Force - {str(minTour)[:8]} km", self.cities, xpath, ypath)
        print(f"Path followed -> {bruteForce}\nTour Length -> {minTour}")
        return brutePath




if __name__ == "__main__":
    TSP()
    print()