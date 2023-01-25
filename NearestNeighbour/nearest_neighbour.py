

def nearestNeighbour(cities):
    """
    getting the nearest city from another city to calculate the path
    """
    path = [0] * (len(cities) + 1)

    latestCity = 0
    visited = 1  # starting at city 0

    while visited < len(cities):
        # print()
        minPath = float('inf')
        city1 = cities[latestCity]

        for i in range(len(cities)):
            if i in path: continue
            city2 = cities[i]
            # print(f"({latestCity}) -> ({i}) -- {city1.distance(city2)}")

            if city1.distance(city2) < minPath:
                # choosing the city with the least distance from the latestCity we're at
                path[visited] = i
                minPath = city1.distance(city2)

        latestCity = path[visited]
        visited += 1

    return path