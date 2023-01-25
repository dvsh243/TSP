import random

def getRandomPath(cities):
    path = [0] * (len(cities) + 1)

    visited = 1

    while visited < len(cities):

        nextCity = 0
        while nextCity in path:
            nextCity = random.randint(0, len(cities) - 1)
        # print(f"nextCity chosen -> {nextCity}")

        path[visited] = nextCity
        visited += 1
    
    return path