from shapely.geometry import Point
import minBoundingCircle as mbc


def getMinBoundingCircle(district):

    coords = district.coordPairs
    x, y, radius = mbc.make_circle(coords)
    return Point(x, y).buffer(radius)
