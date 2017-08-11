import minBoundingCircle as mbc
import math
import pandas as pd
from shapely.geometry import Polygon, MultiPolygon


def getMinBoundingCircleAreas(districtObject):
    areas = []
    for coords in districtObject.coordPairs:
        x, y, radius = mbc.make_circle(coords)
        area = math.pi * radius**2
        areas.append(area)
    if len(areas) > 1:
        areas = pd.Series(areas)
    return areas


def getConvexHullArea(districtObject):
    area = districtObject.gdf.convex_hull.area
    return area


def getCoordPairs(gdf):
    allShapeCoords = []
    for i, row in gdf.iterrows():
        coordPairs = []
        if type(row['geometry']) == Polygon:
            x, y = gdf.geometry[0].exterior.coords.xy
            coordPairs = zip(x, y)
        elif type(row['geometry']) == MultiPolygon:
            for polygon in row.geometry:
                x, y = polygon.exterior.coords.xy
                coordPairs += zip(x, y)
        allShapeCoords += [coordPairs]
    return allShapeCoords
