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


def scoresToGeojson(District, metricName, path_out=None):
    if metricName == 'polsbypopper':
        District.gdf['polsbypopper'] = calculatePolsbyPopper(District)
    elif metricName == 'schwarzberg':
        District.gdf['schwarzberg'] = calculateSchwartzberg(District)
    elif metricName == 'convex_hull':
        District.gdf['convex_hull'] = calculateConvexHull(District)
    elif metricName == 'reock':
        District.gdf['reock'] = calculateReock(District)
    else:
        raise Warning(
            'Plese specify a legitimate metric name!'
            'Here are some good examples: {0}'.format(str(District.metrics))
        )
    District.gdf = District.gdf.to_crs({'init': District.inCrs})
    jsonDistrict = District.gdf.to_json()
    if path_out:
        with open(path_out, 'wb') as f:
            f.write(jsonDistrict)
    else:
        return District.gdf.to_json()
