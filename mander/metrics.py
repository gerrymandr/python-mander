import math


def calculatePolsby(district):
    ppScore = 4 * math.pi * district.area / district.length**2
    return ppScore
