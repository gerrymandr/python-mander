# mander
Python package for calculating metrics related to district shapes.

# Example

```python
from mander import District

district = District(geojson_polygon)

pp_score = district.calculatePolsbyPopper()
```

# Compactness Metrics
This package can calculate compactness statistics for three commonly-used ratios to measure potential gerrymandering.

## Polsby-Popper
The Polsby-Popper measure is a ratio of the area of the district to the area of a circle whose circumference is equal to the perimeter of the district.

The formula for calculating the Polsby-Popper score is:  
![](https://github.com/cicero-data/compactness-stats/raw/master/img/polsby-popper-formula.png)

where A is the area of the district and p is the perimeter of the district.

## Convex Hull


## Reock
