Mander
======

A Python package and command line utility for calculating compactness metrics of
electoral districts.



Example
=======

What scores are available?

    import mander
    mander.getListOfScores()

Getting scores for GeoJSON:

    import mander

    geojson_data = """{ "type": "FeatureCollection", "features": [{"type": "Feature","properties": {},"geometry": { "type": "Polygon", "coordinates": [ [ [ -30.585937499999996, 27.68352808378776 ], [ -2.8125, 27.68352808378776 ], [ -2.8125, 46.800059446787316 ], [ -30.585937499999996, 46.800059446787316 ], [ -30.585937499999996, 27.68352808378776 ] ] ] } } ] }"""

    mander.getScoresForGeoJSON(geojson_data)

Augmenting an existing shapefile with compactness scores:

    import mander
    mander.augmentShapefileWithScores("us_electoral_districts.shp")



Compactness Metrics
===================

Scores are calculated using the underlying
[compactnesslib](https://github.com/r-barnes/compactnesslib)
a list of the scores available and how they are calculated is available
[here](https://github.com/r-barnes/compactnesslib/blob/master/Scores.md).



Credits
=======

This package was created for the
[Metric Geometry And Gerrymandering Group](https://sites.tufts.edu/gerrymandr/)
as part of a hack-a-thon on August 10-11, 2017.