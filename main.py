import time

from utils import generateCities, visualizePath, getPathCoords
from BruteForce.brute_force import bruteForce
from BruteForce.brute_force_worst import bruteForceWorst




start_time = time.perf_counter()
N = 8  # dont go beyong 9 for brute force
cities = generateCities(N)
    

print(f" ---- BRUTE FORCE (WORST) ----")
minTour, bestPath = bruteForceWorst(cities)
print(f"time taken for {N} cities -> {str(time.perf_counter() - start_time)[:7]} seconds.")
xpath, ypath = getPathCoords(bestPath, cities)
visualizePath(f"Brute Force (WORST) - {str(minTour)[:8]} km", cities, xpath, ypath)


print("\n")


print(f" ---- BRUTE FORCE ----")
minTour, bestPath = bruteForce(cities)
print(f"time taken for {N} cities -> {str(time.perf_counter() - start_time)[:7]} seconds.")
xpath, ypath = getPathCoords(bestPath, cities)
visualizePath(f"Brute Force - {str(minTour)[:8]} km", cities, xpath, ypath)


print("\n")


input("Press any key to close : ")