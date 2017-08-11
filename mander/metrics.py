import math
import utils
import numpy as np


def calculatePolsbyPopper(district):
    ppScore = 4 * math.pi * district.area / district.perimeter**2
    return ppScore


def calculateConvexHull(district):
    chArea = utils.getConvexHullArea(district)
    chScore = district.area / chArea
    return chScore


def calculateReock(district):
    mbcArea = utils.getMinBoundingCircleArea(district)
    reockScore = district.area / mbcArea
    return reockScore


def calculateSchwartzberg(district):
    r = np.sqrt((district.area) / math.pi)
    c = 2 * math.pi * r
    score = 1 / (district.perimeter / c)
    return score
