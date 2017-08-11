import geopandas as gpd
import utils


class District(object):

    def __init__(self, path=None, json=None, inCrs='epsg:4326',
                 metricCrs='epsg:2163'):
        """
        Instantiates a District object with either a path to GeoJSON/shapefile
        or an in-memory GeoJSON object. If both are specified the in-memory
        object will take precedence.
        """
        if json is not None and isinstance(json, dict):
            self.gdf = gpd.GeoDataFrame.from_features(json['features'])
        elif path is not None and isinstance(path, basestring):
            self.gdf = gpd.read_file(path)
        else:
            raise KeyError("No path or JSON object supplied.")
        self.inCrs = inCrs
        self.metricCrs = metricCrs
        self.gdf.crs = {'init': inCrs}
        self.gdf = self.gdf.to_crs({'init': metricCrs})
        self.area = self.gdf.area
        self.perimeter = self.gdf.length
        self.coordPairs = utils.getCoordPairs(self.gdf)
        self.metrics = ['polsby_popper', 'schwarzberg', 'convex_hull', 'reock']
