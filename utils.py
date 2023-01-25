import random
import math
import matplotlib.pyplot as plt


class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, city):
        """Get distance (hypotenuse) between city1 and city2"""
        dx = self.x - city.x
        dy = self.y - city.y
        return math.sqrt(dx ** 2 + dy ** 2)


def generateCities(N):
    cities = []
    for i in range(N):
        cities.append(
            City(
                x = random.randint(0, 1000),
                y = random.randint(0, 1000),
            )
        )
    return cities


def getPathCoords(path, cities):
    """
    path: list -> [1, 0, 3, 2, 4]
    """
    x_list, y_list = [], []

    for i in path:
        x_list.append( cities[i].x )
        y_list.append( cities[i].y )
    
    return x_list, y_list


def getPathLength(path, cities):
    pathLength = 0
    for i in range(len(path) - 1):
        city1, city2 = cities[ path[i] ], cities[ path[i+1] ]
        pathLength += city1.distance(city2)
    return pathLength


def visualizeCities(cities):
    fig = plt.figure()
    fig.suptitle('cities')

    x_list, y_list = [], []
    for city in cities:
        x_list.append(city.x)
        y_list.append(city.y)

    plt.scatter(x = x_list, y = y_list)

    plt.show()


def visualizePath(title, cities, xpath, ypath):

    fig = plt.figure()
    fig.suptitle(title)

    x_list, y_list = [], []
    for city in cities:
        x_list.append(city.x)
        y_list.append(city.y)

    plt.scatter(x = x_list, y = y_list)
    plt.plot(xpath, ypath)

    plt.show(block = False)



if __name__ == "__main__":

    cities = generateCities(14)
    visualizeCities(cities)
