import time

from utils import generateCities, visualizePath, getPathCoords, getPathLength
from BruteForce.brute_force import bruteForce
from BruteForce.brute_force_worst import bruteForceWorst
from NearestNeighbour.nearest_neighbour import nearestNeighbour
from Random.random_route import getRandomPath
from Swapping.two_opt import twoOptSwap
from Swapping.three_opt import threeOptSwap


visualize = False
SWAP_COUNT = 10000
CITY_COUNT = 40
# (for 3 opt swap) 3 > N < 9 (for brute force)

RANDOM_PATH = True
NEAREST_NEIGHBOUR = False
TWO_OPT = True
THREE_OPT = True
BRUTE_FORCE = False

print("\n")

cities = generateCities(CITY_COUNT)


if RANDOM_PATH:
    print(f" ---- RANDOM PATH ---- ")
    start_time = time.perf_counter()
    randomPath = getRandomPath(cities)
    tourLength = getPathLength(randomPath, cities)
    xpath, ypath = getPathCoords(randomPath, cities)
    # print(f"time taken for {CITY_COUNT} cities -> {str(time.perf_counter() - start_time)[:7]} seconds.")
    if visualize: visualizePath(f"Random Path - {str(tourLength)[:8]} km", cities, xpath, ypath)
    # print(f"Path chosen -> {randomPath}")
    print(f"Tour Length -> {tourLength}")


    print()


if NEAREST_NEIGHBOUR:
    print(f" ---- NEAREST NEIGHBOUR ---- ")
    start_time = time.perf_counter()
    NNPath = nearestNeighbour(cities)
    tourLength = getPathLength(NNPath, cities)
    # print(f"time taken for {CITY_COUNT} cities -> {str(time.perf_counter() - start_time)[:7]} seconds.")
    xpath, ypath = getPathCoords(NNPath, cities)
    if visualize: visualizePath(f"Nearest Neighbour - {str(tourLength)[:8]} km", cities, xpath, ypath)
    # print(f"Path chosen -> {NNPath}")
    print(f"Tour Length -> {tourLength}")


    print()


if TWO_OPT:
    print(f" ---- 2 OPT SWAP ---- ")
    start_time = time.perf_counter()
    minTour, bestPath = twoOptSwap(randomPath, cities, N=SWAP_COUNT)
    # print(f"time taken for {CITY_COUNT} cities -> {str(time.perf_counter() - start_time)[:7]} seconds.")
    xpath, ypath = getPathCoords(bestPath, cities)
    if visualize: visualizePath(f"2 Opt Swap - {str(minTour)[:8]} km", cities, xpath, ypath)
    # print(f"Path chosen -> {bestPath}")
    print(f"Tour Length -> {minTour}")


    print()
    

if THREE_OPT:
    print(f" ---- 3 OPT SWAP ---- ")
    start_time = time.perf_counter()
    minTour, bestPath = threeOptSwap(randomPath, cities, N=SWAP_COUNT)
    # print(f"time taken for {CITY_COUNT} cities -> {str(time.perf_counter() - start_time)[:7]} seconds.")
    xpath, ypath = getPathCoords(bestPath, cities)
    if visualize: visualizePath(f"3 Opt Swap - {str(minTour)[:8]} km", cities, xpath, ypath)
    # print(f"Path chosen -> {bestPath}")
    print(f"Tour Length -> {minTour}")



    print()    




if BRUTE_FORCE:
    print(f" ---- BRUTE FORCE ---- ")
    start_time = time.perf_counter()
    minTour, bestPath = bruteForce(cities)
    print(f"time taken for {CITY_COUNT} cities -> {str(time.perf_counter() - start_time)[:7]} seconds.")
    xpath, ypath = getPathCoords(bestPath, cities)
    if visualize: visualizePath(f"Brute Force - {str(minTour)[:8]} km", cities, xpath, ypath)
    print(f"Path chosen -> {bestPath}")
    print(f"Tour Length -> {minTour}")


    print()


# print(f" ---- BRUTE FORCE (WORST) ---- ")
# start_time = time.perf_counter()
# minTour, bestPath = bruteForceWorst(cities)
# print(f"time taken for {CITY_COUNT} cities -> {str(time.perf_counter() - start_time)[:7]} seconds.")
# xpath, ypath = getPathCoords(bestPath, cities)
# if visualize: visualizePath(f"Brute Force (WORST) - {str(minTour)[:8]} km", cities, xpath, ypath)
# print(f"Path chosen -> {bestPath}")
# print(f"Tour Length -> {minTour}")


# print()




if visualize: input("Press any key to close : ")