import math
import utils
import numpy as np


def calculatePolsbyPopper(District):
    ppScore = 4 * math.pi * District.area / District.perimeter**2
    return ppScore


def calculateConvexHull(District):
    chArea = utils.getConvexHullArea(District)
    chScore = District.area / chArea
    return chScore


def calculateReock(District):
    mbcAreas = utils.getMinBoundingCircleAreas(District)
    reockScore = District.area / mbcAreas
    return reockScore


def calculateSchwartzberg(District):
    r = np.sqrt((District.area) / math.pi)
    c = 2 * math.pi * r
    score = 1 / (District.perimeter / c)
    return score


def scoresToGeojson(District, metricName):
    if metricName == 'polsby':
        District.gdf['polsby'] = calculatePolsbyPopper(District)
    elif metricName == 'schwarzberg':
        District.gdf['schwarzberg'] = calculateSchwartzberg(District)
    elif metricName == 'convex_hull':
        District.gdf['convex_hull'] = calculateConvexHull(District)
    elif metricName == 'reock':
        District.gdf['reock'] = calculateReock(District)
    return District.to_json()
