from shapely.geometry import Point
import minBoundingCircle as mbc
import math


def getMinBoundingCircleArea(district):

    coords = district.coordPairs
    x, y, radius = mbc.make_circle(coords)
    area = math.pi * radius**2
    return area


def getConvexHullArea(district):
    area = district.gdf.convex_hull.area
    return area


def getCoordPairs(gdf):

    coordPairs = []
    if gdf.geom_type[0] == 'Polygon':
        x, y = gdf.geometry[0].exterior.coords.xy
        coordPairs = zip(x, y)
    elif gdf.geom_type[0] == 'MultiPolygon':
        for polygon in gdf.geometry[0]:
            x, y = polygon.exterior.coords.xy
            coordPairs += zip(x, y)
    return coordPairs

