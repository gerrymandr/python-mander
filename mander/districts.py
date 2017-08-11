import geopandas as gpd
import utils


class District(object):

    def __init__(self, pathToGeojsonOrShapefile, inCrs='epsg:4326',
                 outCrs='epsg:2163'):
        self.epsg = outCrs.split(':')[1]
        self.gdf = gpd.read_file(pathToGeojsonOrShapefile)
        self.gdf.crs = {'init': inCrs}
        self.gdf = self.gdf.to_crs(epsg=self.epsg)
        self.area = self.gdf.area.values[0]
        self.perimeter = self.gdf.length.values[0]
        self.coordPairs = utils.getCoordPairs(self.gdf)


class Delegation(object):

    def __init__(self, pathToGeojsonOrShapefile, inCrs='epsg:4326',
                 outCrs='epsg:2163'):
        self.epsg = outCrs.split(':')[1]
        self.gdf = gpd.read_file(pathToGeojsonOrShapefile)
        self.gdf.crs = {'init': inCrs}
        self.gdf = self.gdf.to_crs(epsg=self.epsg)
        self.gdf['area'] = self.gdf.area
        self.gdf['perimeter'] = self.gdf.length
        self.area = self.gdf.area
        self.perimeter = self.gdf.length
        self.coordPairs = utils.getCoordPairs(self.gdf)
