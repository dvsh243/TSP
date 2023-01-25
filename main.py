import time

from utils import generateCities, visualizePath, getPathCoords, getPathLength
from BruteForce.brute_force import bruteForce
from BruteForce.brute_force_worst import bruteForceWorst
from NearestNeighbour.nearest_neighbour import nearestNeighbour


print("\n")

N = 8  # dont go beyong 9 for brute force
cities = generateCities(N)
    

# print(f" ---- BRUTE FORCE (WORST) ---- ")
# start_time = time.perf_counter()
# minTour, bestPath = bruteForceWorst(cities)
# print(f"time taken for {N} cities -> {str(time.perf_counter() - start_time)[:7]} seconds.")
# xpath, ypath = getPathCoords(bestPath, cities)
# visualizePath(f"Brute Force (WORST) - {str(minTour)[:8]} km", cities, xpath, ypath)
# print(f"Path chosen -> {bestPath}")


# print("\n")


print(f" ---- BRUTE FORCE ---- ")
start_time = time.perf_counter()
minTour, bestPath = bruteForce(cities)
print(f"time taken for {N} cities -> {str(time.perf_counter() - start_time)[:7]} seconds.")
xpath, ypath = getPathCoords(bestPath, cities)
visualizePath(f"Brute Force - {str(minTour)[:8]} km", cities, xpath, ypath)
print(f"Path chosen -> {bestPath}")


print("\n")


print(f" ---- NEAREST NEIGHBOUR ---- ")
start_time = time.perf_counter()
bestPath = nearestNeighbour(cities)
tourLength = getPathLength(bestPath, cities)
print(f"time taken for {N} cities -> {str(time.perf_counter() - start_time)[:7]} seconds.")
xpath, ypath = getPathCoords(bestPath, cities)
visualizePath(f"Nearest Neighbour - {str(tourLength)[:8]} km", cities, xpath, ypath)
print(f"Path chosen -> {bestPath}")


print("\n")


input("Press any key to close : ")