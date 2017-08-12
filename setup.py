from setuptools import setup, Extension
#from distutils.core import setup, Extension
import glob

ext_modules = [
  Extension(
    "compactnesslib",
    glob.glob('src/*.cpp') + glob.glob('lib/compactnesslib/src/*.cpp'),
    include_dirs = ['lib/compactnesslib/src', 'lib/pybind11/'],
    language = 'c++',
    extra_compile_args = ['-std=c++17'],
    define_macros = [('DOCTEST_CONFIG_DISABLE',None)]
  )
]

setup(name='mander',
  version      = '0.1',
  description  = 'Python package to calculate compactness metrics for district shapes.',
  url          = 'http://github.com/gerrymandr/python-mander',
  author       = 'Geometry of Redistricting Workshop',
  author_email = '',
  license      = 'MIT',
  ext_modules  = ext_modules
)
