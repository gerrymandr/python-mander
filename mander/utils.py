import minBoundingCircle as mbc
import math
import pandas as pd


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
        if gdf.geom_type[0] == 'Polygon':
            x, y = gdf.geometry[0].exterior.coords.xy
            coordPairs = zip(x, y)
        elif gdf.geom_type[0] == 'MultiPolygon':
            for polygon in gdf.geometry[0]:
                x, y = polygon.exterior.coords.xy
                coordPairs += zip(x, y)
        allShapeCoords += [coordPairs]
    return allShapeCoords
