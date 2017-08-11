import geopandas as gpd
import utils

class District(object):

    def __init__(self, path=None, json=None, epsg='2163'):
        """
        Instantiates a District object with either a path to GeoJSON/shapefile
        or an in-memory GeoJSON object. If both are specified the in-memory
        object will take precedence.
        """

        self.epsg = epsg
        if json is not None and isinstance(json, dict):
            self.gdf = gpd.GeoDataFrame.from_features(json['features'])
        elif path is not None and isinstance(path, basestring):
            self.gdf = gpd.read_file(path)
        else:
            raise KeyError("No path or JSON object supplied.")
        if not self.gdf.crs:
            self.gdf.crs = {'init': 'epsg:4326'}
        self.gdf = self.gdf.to_crs(epsg=self.epsg)
        self.area = self.gdf.area.values[0]
        self.perimeter = self.gdf.length.values[0]
        self.coordPairs = utils.getCoordPairs(self.gdf)
