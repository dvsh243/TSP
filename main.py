import time

from utils import generateCities, visualizePath, getPathCoords, getPathLength
from BruteForce.brute_force import bruteForce
from BruteForce.brute_force_worst import bruteForceWorst
from NearestNeighbour.nearest_neighbour import nearestNeighbour
from Random.random_route import getRandomPath
from LocalSearch.two_opt import twoOptSwap
from LocalSearch.three_opt import threeOptSwap
from SimulatedAnnealing.anneal import SimAnneal



class TSP:

    def __init__(self):

        self.VISUALIZE = True
        self.CITY_COUNT = 11  # (for 3 opt swap) 3 > N < 9 (for brute force)

        # - # - # - # - # - # - # - # - # - # - 
        self.BRUTE_FORCE = True
        self.RANDOM_PATH = True
        self.NEAREST_NEIGHBOUR = True
        self.SIMULATED_ANNEALING = True
        
        self.SWAP_COUNT = 200
        self.TWO_OPT = True
        self.THREE_OPT = True
        # - # - # - # - # - # - # - # - # - # - 

        self.cities = generateCities(self.CITY_COUNT)

        randomPath = self.randomPathTSP()
        # NNPath = self.nearestNeighbourTSP()
        # brutePath = self.bruteForceTSP()
        twoOptPath = self.twoOptTSP(randomPath)
        # threeOptPath = self.threeOptTSP(randomPath)
        simAnnealPath = self.SimulatedAnnealingTSP(randomPath)

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
        print(f"Path followed -> {brutePath}\nTour Length -> {minTour}")
        return brutePath


    def SimulatedAnnealingTSP(self, optPath):
        if not self.SIMULATED_ANNEALING: return None

        print("\n ---- SIMULATED ANNEALING ---- ")
        annealObj = SimAnneal(self.cities, optPath, decay=0.98)
        minPath = getPathLength(annealObj.path, self.cities)
        xpath, ypath = getPathCoords(annealObj.path, self.cities)
        if self.VISUALIZE: visualizePath(f"Simulated Annealing - {str(minPath)[:8]} km", self.cities, xpath, ypath)
        print(f"Path followed -> {annealObj.path}\nTour Length -> {minPath}")
        return annealObj.path




if __name__ == "__main__":
    TSP()
    print()