from os import path, getcwd
import json
import copy

from unittest import TestCase

#import geopandas
from mander.districts import District
from mander.metrics import calculatePolsby, calculateConvexHull, calculateReock, calculateSchwartzberg

base_dir = path.dirname(path.realpath(__file__))

test_districts = ['CD_CA_9', 'CD_IL_4', 'CD_PA_7', 'CD_CA_24', 'CD_MA_9']

metrics = {
    'polsbypopper': [],
    'convexhull': [],
    'reock': [],
    'schwartzberg': []
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

      test_district = District(district_boundaries_file) # TODO use python object instead of file path parameter

      # Polsby Popper
      test_expected['polsbypopper'].append('%.4f' % district_scores['polsbypopper'])
      test_results['polsbypopper'].append('%.4f' % calculatePolsby(test_district))

      # Convex Hull
      test_expected['convexhull'].append('%.4f' % district_scores['convexhull'])
      test_results['convexhull'].append('%.4f' % calculateConvexHull(test_district))

      # Reock
      test_expected['reock'].append('%.4f' % district_scores['convexhull'])
      test_results['reock'].append('%.4f' % calculateReock(test_district))

      # Schwartzberg
      test_expected['schwartzberg'].append('%.4f' % district_scores['schwartzberg'])
      test_results['schwartzberg'].append('%.4f' % calculateSchwartzberg(test_district))


class TestMetrics(TestCase):

    def test_polsbypopper(self):
      self.assertEqual(test_expected['polsbypopper'], test_results['polsbypopper'])

    def test_convexhull(self):
      self.assertEqual(test_expected['convexhull'], test_results['convexhull'])

    def test_reock(self):
      self.assertEqual(test_expected['reock'], test_results['reock'])

    def test_schwartzberg(self):
      self.assertEqual(test_expected['schwartzberg'], test_results['schwartzberg'])
