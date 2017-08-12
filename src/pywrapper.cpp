#include <compactnesslib.hpp>
#include <pybind11.h>

namespace py = pybind11;

//Tutorials
//http://www.benjack.io/2017/06/12/python-cpp-tests.html
//https://pybind11.readthedocs.io/en/stable/classes.html
//http://people.duke.edu/~ccc14/sta-663-2016/18G_C++_Python_pybind11.html

std::string ProcessGeoJSON(const std::string &geojson, const std::string id){
  auto gc = complib::ReadGeoJSON(geojson);
  complib::CalculateAllScores(gc);
  return complib::OutScoreJSON(gc, id);
}


PYBIND11_PLUGIN(compactnesslib) {
  py::module m("compactnesslib", "Gerrymandering score calculator");

  m.def(
    "ProcessGeoJSON",
    &ProcessGeoJSON,
    "Takes a GeoJSON string as input, calculates all scores, return a JSON dictionary of the scores keyed to values identified 'id' which are expected to be properties of the GeoJSON objects. If id='', then the object's 0-indexed order is used.",
    py::arg("geojson"),
    py::arg("id")=""
  );

  return m.ptr();
}