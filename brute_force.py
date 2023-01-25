from utils import generateCities, visualizePath
import matplotlib.pyplot as plt
import time


def bruteForce(cities):
    """
    computing permutations of all possible paths
    permutation [0, 3, 1, 2] means (0) -> (3) -> (1) -> (2) -> (0) 
    ```for path in itertools.permutations( range(len(cities)) ):```
    """

    permutations = permute( [i for i in range(len(cities))] )
    print(f"total {len(permutations)} to compute.")
    
    minTour, bestPath = float('inf'), None
    # minTour, bestPath = 0, None  # uncomment and change sign (tourLength > minTour) for worst path
    
    progress = 0
    for path in permutations:
        progress += 1
        tourLength = 0

        for i in range(len(path)):
            city, next_city = cities[ path[i] ], cities[ path[(i+1) % len(path)] ]
            tourLength += city.distance(next_city)
        
        if tourLength < minTour:
            bestPath = path
            minTour = tourLength
        
        if progress % 10000 == 0: print(f"{str(progress / len(permutations) * 100)[:5]}% permutations computed.", end='\r')
    
    return minTour, bestPath




def bruteForceWorst(cities):
    """
    brute force but for the worst path possible instead of the best
    (THIS CODE IS NOT TO BE ADDED IN FINAL PROJECT)
    """

    permutations = permute( [i for i in range(len(cities))] )
    print(f"total {len(permutations)} to compute.")
    
    minTour, bestPath = 0, None
    
    progress = 0
    for path in permutations:
        progress += 1
        tourLength = 0

        for i in range(len(path)):
            city, next_city = cities[ path[i] ], cities[ path[(i+1) % len(path)] ]
            tourLength += city.distance(next_city)
        
        if tourLength > minTour:
            bestPath = path
            minTour = tourLength
        
        if progress % 10000 == 0: print(f"{str(progress / len(permutations) * 100)[:5]}% permutations computed.", end='\r')
    
    return minTour, bestPath




def getPathCoords(path, cities):
    x_list, y_list = [], []

    for i in path:
        x_list.append( cities[i].x )
        y_list.append( cities[i].y )
    
    return x_list, y_list


def permute(nums):
    permutations = []

    def dfs(index, left, path):
        if index == len(nums):
            permutations.append( path )
            return

        for i in range(len(left)):
            dfs(
                index + 1, 
                left[:i] + left[i+1:],
                path + [left[i]]
            )

    dfs(0, nums, [])
    return permutations



if __name__ == "__main__":
    start_time = time.perf_counter()
    N = 8  # dont go beyong 9
    
    cities = generateCities(N)
    minTour, bestPath = bruteForce(cities)

    print(f"time taken for {N} cities -> {str(time.perf_counter() - start_time)[:7]} seconds.")

    xpath, ypath = getPathCoords(bestPath, cities)
    visualizePath(f"Brute Force - {str(minTour)[:8]} km", cities, xpath, ypath)


    # WORST PATH
    minTour, bestPath = bruteForceWorst(cities)
    xpath, ypath = getPathCoords(bestPath, cities)
    visualizePath(f"Brute Force (WORST) - {str(minTour)[:8]} km", cities, xpath, ypath)
