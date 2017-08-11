from setuptools import setup, find_packages

setup(name='mander',
  version='0.2',
  description='Python package to calculate compactness metrics for district shapes.',
  url='http://github.com/gerrymandr/python-mander',
  author='Geometry of Redistricting Workshop',
  author_email='gerrymandr@gmail.com',
  license='MIT',
  packages=find_packages(exclude=['contrib', 'docs', 'tests*'])
)
