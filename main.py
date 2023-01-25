import time

from utils import generateCities, visualizePath, getPathCoords, getPathLength
from BruteForce.brute_force import bruteForce
from BruteForce.brute_force_worst import bruteForceWorst
from NearestNeighbour.nearest_neighbour import nearestNeighbour
from Random.random_route import getRandomPath
from Swapping.two_opt import twoOptSwap


visualize = True

print("\n")

N = 8
# (for 2 opt swap) 2 > N < 9 (for brute force)
cities = generateCities(N)


print(f" ---- RANDOM PATH ---- ")
start_time = time.perf_counter()
randomPath = getRandomPath(cities)
tourLength = getPathLength(randomPath, cities)
xpath, ypath = getPathCoords(randomPath, cities)
print(f"time taken for {N} cities -> {str(time.perf_counter() - start_time)[:7]} seconds.")
if visualize: visualizePath(f"Random Path - {str(tourLength)[:8]} km", cities, xpath, ypath)
print(f"Path chosen -> {randomPath}")
print(f"Tour Length -> {tourLength}")


print()


print(f" ---- 2 OPT SWAP ---- ")
start_time = time.perf_counter()
minTour, bestPath = twoOptSwap(randomPath, cities, N=50)
print(f"time taken for {N} cities -> {str(time.perf_counter() - start_time)[:7]} seconds.")
xpath, ypath = getPathCoords(bestPath, cities)
if visualize: visualizePath(f"Two Opt Swap - {str(minTour)[:8]} km", cities, xpath, ypath)
print(f"Path chosen -> {bestPath}")
print(f"Tour Length -> {minTour}")


print()
    

# print(f" ---- BRUTE FORCE (WORST) ---- ")
# start_time = time.perf_counter()
# minTour, bestPath = bruteForceWorst(cities)
# print(f"time taken for {N} cities -> {str(time.perf_counter() - start_time)[:7]} seconds.")
# xpath, ypath = getPathCoords(bestPath, cities)
# if visualize: visualizePath(f"Brute Force (WORST) - {str(minTour)[:8]} km", cities, xpath, ypath)
# print(f"Path chosen -> {bestPath}")
# print(f"Tour Length -> {minTour}")


# print()


# print(f" ---- BRUTE FORCE ---- ")
# start_time = time.perf_counter()
# minTour, bestPath = bruteForce(cities)
# print(f"time taken for {N} cities -> {str(time.perf_counter() - start_time)[:7]} seconds.")
# xpath, ypath = getPathCoords(bestPath, cities)
# if visualize: visualizePath(f"Brute Force - {str(minTour)[:8]} km", cities, xpath, ypath)
# print(f"Path chosen -> {bestPath}")
# print(f"Tour Length -> {minTour}")


# print()


# print(f" ---- NEAREST NEIGHBOUR ---- ")
# start_time = time.perf_counter()
# bestPath = nearestNeighbour(cities)
# tourLength = getPathLength(bestPath, cities)
# print(f"time taken for {N} cities -> {str(time.perf_counter() - start_time)[:7]} seconds.")
# xpath, ypath = getPathCoords(bestPath, cities)
# if visualize: visualizePath(f"Nearest Neighbour - {str(tourLength)[:8]} km", cities, xpath, ypath)
# print(f"Path chosen -> {bestPath}")
# print(f"Tour Length -> {tourLength}")


# print()


if visualize: input("Press any key to close : ")