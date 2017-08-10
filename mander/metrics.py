import math


def calculatePolsby(district):
    ppScore = 4 * math.pi * district.area / district.length**2
    return ppScore


def calculateConvexHull(district):
    chScore = district.area / district.convex_hull.area
    return chScore
