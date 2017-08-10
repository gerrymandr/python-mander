from os import path, getcwd
import json
import copy

from unittest import TestCase

#import geopandas
from mander.districts import district
from mander.metrics import calculatePolsby

base_dir = path.dirname(path.realpath(__file__))

test_districts = ['CD_CA_24', 'CD_CA_9', 'CD_IL_4', 'CD_MA_9', 'CD_PA_7']

metrics = {
    'polsbypopper': []
}

test_expected = copy.deepcopy(metrics)
test_results = copy.deepcopy(metrics)

for d in test_districts:

  district_boundaries_file = path.join(base_dir, 'data', d + '.geojson')
  district_scores_file = path.join(base_dir, 'data', d + '_scores.json')

  with open(district_boundaries_file) as district_boundary_data:
    with open(district_scores_file) as district_scores_data:

      district_boundary = json.load(district_boundary_data)
      district_scores = json.load(district_scores_data)

      test_district = district(district_boundaries_file) # TODO use python object instead of file path parameter

      # Polsby Popper
      test_expected['polsbypopper'].append(district_scores['polsbypopper'])
      test_results['polsbypopper'].append(calculatePolsby(test_district))

print(test_expected)
print(test_results)

class TestMetrics(TestCase):

    def test_polsbypopper(self):
      self.assertEqual(test_expected['polsbypopper'], test_results['polsbypopper'])
