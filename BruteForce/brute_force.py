from utils import getPathCoords
import matplotlib.pyplot as plt


def bruteForce(cities, visual = False):
    """
    computing permutations of all possible paths
    permutation [0, 3, 1, 2] means (0) -> (3) -> (1) -> (2) -> (0) 
    ```for path in itertools.permutations( range(len(cities)) ):```
    """

    permutations = permute( [i for i in range(len(cities))] )
    print(f"total {len(permutations)} to compute.")
    
    minTour, bestPath = float('inf'), None
    # minTour, bestPath = 0, None  # uncomment and change sign (tourLength > minTour) for worst path
    
    xpath, ypath = getPathCoords(permutations[0] + [0], cities)
    
    progress = 0
    for path in permutations:

        if visual:
            plt.scatter(xpath, ypath)
            plt.suptitle(f" Brute Force ({progress}) - {minTour} km")
            for i in range(len(cities)): plt.annotate(i, (xpath[i], ypath[i]))
            xpath, ypath = getPathCoords(path + [0], cities)
            plt.plot(xpath, ypath)
            plt.pause(0.01)
            plt.clf()

        progress += 1
        tourLength = 0

        for i in range(len(path)):
            city, next_city = cities[ path[i] ], cities[ path[(i+1) % len(path)] ]
            tourLength += city.distance(next_city)
        
        if tourLength < minTour:
            bestPath = path
            minTour = tourLength
        
        if progress % 10000 == 0: print(f"{str(progress / len(permutations) * 100)[:5]}% permutations computed.", end='\r')
    
    return minTour, bestPath + [bestPath[0]]  # connecting last city to the first city


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