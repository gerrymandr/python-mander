import math
import utils
import numpy as np


def calculatePolsbyPopper(districtObject):
    ppScore = 4 * math.pi * districtObject.area / districtObject.perimeter**2
    return ppScore


def calculateConvexHull(districtObject):
    chArea = utils.getConvexHullArea(districtObject)
    chScore = districtObject.area / chArea
    return chScore


def calculateReock(districtObject):
    mbcAreas = utils.getMinBoundingCircleAreas(districtObject)
    reockScore = districtObject.area / mbcAreas
    return reockScore


def calculateSchwartzberg(districtObject):
    r = np.sqrt((districtObject.area) / math.pi)
    c = 2 * math.pi * r
    score = 1 / (districtObject.perimeter / c)
    return score


def getDelegationScores(Delegation, metricName):
    if metricName == 'polsby':
        Delegation.gdf['polsby'] = calculatePolsby(Delegation)
    elif metricName == 'schwarzberg':
        Delegation.gdf['schwarzberg'] = calculateSchwartzberg(Delegation)
    elif metricName == 'convex_hull':
        Delegation.gdf['convex_hull'] = calculateConvexHull(Delegation)
    elif metricName == 'reock':
        Delegation.gdf['reock'] = calculateReock(Delegation)
    return Delegation
