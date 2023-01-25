import random
from utils import getPathLength


def twoOptSwap(path, cities, N=100):
    """
    we can't modify 1st and last cities of path
    (path will start at city 0 and end at city 0)
    """
    
    # print(f"og path length -> {getPathLength(path, cities)}\n")
    swapCount = 0
    minTour = getPathLength(path, cities)

    for i in range(N):
        newPath = swapCities(path, cities)
        # print(f"new path length -> {getPathLength(newPath, cities)}")

        if getPathLength(newPath, cities) < minTour:
            minTour = getPathLength(newPath, cities)
            path = newPath
            swapCount += 1

    print(f"Swapped {swapCount} / {N} times to find optimal solution.")
    return minTour, path


def swapCities(path, cities):
    newPath = path.copy()
    u, v = random.randint(1, len(cities)-1), random.randint(1, len(cities)-1)
    while u == v:
        v = random.randint(1, len(cities)-1)
    
    # print(f"two cities to swap -- ({path[u]}) <-> ({path[v]})")
    newPath[v], newPath[u] = path[u], path[v]

    return newPath


    