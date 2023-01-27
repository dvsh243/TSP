import time

from utils import generateCities, visualizePath, getPathCoords, getPathLength
from BruteForce.brute_force import bruteForce
from BruteForce.brute_force_worst import bruteForceWorst
from NearestNeighbour.nearest_neighbour import nearestNeighbour
from Random.random_route import getRandomPath
from LocalSearch.two_opt import twoOptSwap
from LocalSearch.three_opt import threeOptSwap
from SimulatedAnnealing.anneal import SimAnneal
from AntColony.ant_colony import AntColony



class TSP:

    def __init__(self):

        # - # - # - # - # - # - # - # - # - # - 

        self.VISUALIZE = True
        self.CITY_COUNT = 20  # (for 3 opt swap) 3 > N < 9 (for brute force)
        self.SWAP_COUNT = 80000
        self.cities = generateCities(self.CITY_COUNT)

        # - # - # - # - # - # - # - # - # - # - 

        randomPath = self.randomPathTSP()
        # NNPath = self.nearestNeighbourTSP()
        # brutePath = self.bruteForceTSP()
        twoOptPath = self.twoOptTSP(randomPath, visual=False)
        # threeOptPath = self.threeOptTSP(twoOptPath, visual=False)
        simAnnealPath = self.SimulatedAnnealingTSP(randomPath, visual=False)
        # antColonyPath = self.AntColonyTSP()

        if self.VISUALIZE: input("Enter any key to exit: ")


    def randomPathTSP(self):

        print(f"\n ---- RANDOM PATH ---- ")
        randomPath = getRandomPath(self.cities)
        tourLength = getPathLength(randomPath, self.cities)
        xpath, ypath = getPathCoords(randomPath, self.cities)
        if self.VISUALIZE: visualizePath(f"Random Path - {str(tourLength)[:8]} km", self.cities, xpath, ypath)
        print(f"Path followed -> {randomPath}\nTour Length -> {tourLength}")
        return randomPath
    

    def nearestNeighbourTSP(self):
    
        print(f"\n ---- NEAREST NEIGHBOUR ---- ")
        NNPath = nearestNeighbour(self.cities)
        tourLength = getPathLength(NNPath, self.cities)
        xpath, ypath = getPathCoords(NNPath, self.cities)
        if self.VISUALIZE: visualizePath(f"Nearest Neighbour - {str(tourLength)[:8]} km", self.cities, xpath, ypath)
        print(f"Path followed -> {NNPath}\nTour Length -> {tourLength}")
        return NNPath
    

    def twoOptTSP(self, OptPath: list, visual: bool = False):
    
        print(f"\n ---- 2 OPT SWAP ---- ")
        minTour, twoOptPath = twoOptSwap(OptPath, self.cities, N=self.SWAP_COUNT, visual=visual)
        xpath, ypath = getPathCoords(twoOptPath, self.cities)
        if self.VISUALIZE: visualizePath(f"2 Opt Swap - {str(minTour)[:8]} km", self.cities, xpath, ypath)
        print(f"Path followed -> {twoOptPath}\nTour Length -> {minTour}")
        return twoOptPath

    
    def threeOptTSP(self, OptPath: list, visual: bool = False):

        print(f"\n ---- 3 OPT SWAP ---- ")
        minTour, threeOptPath = threeOptSwap(OptPath, self.cities, N=self.SWAP_COUNT, visual=visual)
        xpath, ypath = getPathCoords(threeOptPath, self.cities)
        if self.VISUALIZE: visualizePath(f"3 Opt Swap - {str(minTour)[:8]} km", self.cities, xpath, ypath)
        print(f"Path followed -> {threeOptPath}\nTour Length -> {minTour}")
        return threeOptPath


    def bruteForceTSP(self):
        
        print(f"\n ---- BRUTE FORCE ---- ")
        minTour, brutePath = bruteForce(self.cities)
        xpath, ypath = getPathCoords(brutePath, self.cities)
        if self.VISUALIZE: visualizePath(f"Brute Force - {str(minTour)[:8]} km", self.cities, xpath, ypath)
        print(f"Path followed -> {brutePath}\nTour Length -> {minTour}")
        return brutePath


    def SimulatedAnnealingTSP(self, optPath, visual = False):
        
        print("\n ---- SIMULATED ANNEALING ---- ")
        annealObj = SimAnneal(self.cities, optPath, decay=0.99996, visual=visual)
        minPath = getPathLength(annealObj.minPath, self.cities)
        xpath, ypath = getPathCoords(annealObj.minPath, self.cities)
        if self.VISUALIZE: visualizePath(f"Simulated Annealing - {str(minPath)[:8]} km", self.cities, xpath, ypath)
        print(f"Path followed -> {annealObj.minPath}\nTour Length -> {minPath}")
        return annealObj.minPath


    def AntColonyTSP(self):

        print("\n ---- ANT COLONY OPTIMIZATION ---- ")
        antObject = AntColony(self.cities)


if __name__ == "__main__":
    TSP()
    print()