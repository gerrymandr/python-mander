from shapely.geometry import Point
import minBoundingCircle as mbc
import math


def getMinBoundingCircleArea(district):

    coords = district.coordPairs
    x, y, radius = mbc.make_circle(coords)
    area = math.pi() * radius**2
    return area
