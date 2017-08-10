from os import path
import json

import unittest

from mander.districts import District
from mander.metrics import calculatePolsby

test_districts = ['CD_CA_24', 'CD_CA_9', 'CD_IL_4', 'CD_MA_9', 'CD_PA_7']

metrics = {
    'polsbypopper': []
}

test_expected = metrics.copy()
test_results = metrics.copy()

for d in test_districts:

  district_boundaries_file = path.join('tests', 'data', d, '.geojson')
  district_scores_file = path.join('tests', 'data', d, '_scores.json')

  with json.load(open(district_boundaries_file)) as district_boundary:
    with json.load(open(district_scores_file)) as district_scores:

      district = District(district_boundary)

      # Polsby Popper
      test_expected['polsbypopper'].append(district_scores['polsbypopper'])
      test_results['polsbypopper'].append(calculatePolsby(district))


class TestMetrics(unittest.TestCase):

    def test_polsbypopper(self):
      self.assertEqual(test_expected['polsbypopper'], test_results['polsbypopper'])
