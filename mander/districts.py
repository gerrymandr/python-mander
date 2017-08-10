import geopandas as gpd


class district(object):

    def __init__(self, geojsonFile):
        self.gdf = gpd.read_file(geojsonFile)
        self.gdf = self.gdf.to_crs(epsg='2163')
        self.area = self.gdf.area
        self.perimeter = self.gdf.length

