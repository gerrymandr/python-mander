# Mander

A Python package and command line utility for calculating compactness metrics of
electoral districts.



# Example

What scores are available?

```python
import mander
mander.getListOfScores()
```

Getting scores for GeoJSON:

```python
import mander

geojson_data = """{ "type": "FeatureCollection", "features": [{"type": "Feature","properties": {},"geometry": { "type": "Polygon", "coordinates": [ [ [ -30.585937499999996, 27.68352808378776 ], [ -2.8125, 27.68352808378776 ], [ -2.8125, 46.800059446787316 ], [ -30.585937499999996, 46.800059446787316 ], [ -30.585937499999996, 27.68352808378776 ] ] ] } } ] }"""

mander.getScoresForGeoJSON(geojson_data)
```

Augmenting an existing shapefile with compactness scores:

```python
import mander
mander.augmentShapefileWithScores("us_electoral_districts.shp")
```


# Compactness Metrics

Compactness scores are calculated using the underlying
[compactnesslib](https://github.com/r-barnes/compactnesslib)
a list of the scores available and how they are calculated is available
[here](https://github.com/r-barnes/compactnesslib/blob/master/Scores.md).


# Developer Setup

## Requirements:

* Python 2
* pip
* A compiler that supports C++ 11.
  * If using GCC, must use version 5 or greater

## Recommended
*  virtualenv

## Steps:

* Fork this repo
* Clone your fork
    ```
    git clone git@github.com:YOUR_USERNAME_HERE/python-mander.git
    ```
* Add the original repo as a remote
    ```
    git remote add upstream git@github.com:gerrymandr/python-mander.git
    ```
* This project depends upon a C++ library sourced from a git submodule. Initialize and update the git submodule.
    ```
    git submodule init
    git submodule update
    ```
* Optionally create and activate a [Python virtual environment](https://virtualenv.pypa.io/en/stable/).
    On Linux or Mac
    ```
    virtualenv env
    source env/bin/activate
    ```
    On Windows
    ```
    virtualenv env
    env\Scripts\activate
    ```

    On any platform, you may exit the virtual environment by running
    ```
    deactivate
    ```
* Install the dependencies
    ```
    pip install -r requirements.txt
    ```
* Build the project
    ```
    python setup.py build
    ```
  * If you need to specify a C compiler other than the default one on your system, you may add an inline environment variable `CC` and set it to the other compiler. For example, on a system with both gcc 4 and gcc 7 installed:
    ```
    CC=gcc-7 python setup.py build
    ```


# Credits

This package was created for the
[Metric Geometry And Gerrymandering Group](https://sites.tufts.edu/gerrymandr/)
as part of a hack-a-thon on August 10-11, 2017.
