#include <compactnesslib.hpp>
#include <pybind11.h>
#include <stl.h>
#include <vector>

namespace py = pybind11;

//Tutorials
//http://www.benjack.io/2017/06/12/python-cpp-tests.html
//https://pybind11.readthedocs.io/en/stable/classes.html
//http://people.duke.edu/~ccc14/sta-663-2016/18G_C++_Python_pybind11.html

std::string getUnboundedScoresForGeoJSON(const std::string &geojson, const std::string id, const std::vector<std::string> &score_list){
  auto gc = complib::ReadGeoJSON(geojson);
  complib::CalculateListOfUnboundedScores(gc, score_list);
  return complib::OutScoreJSON(gc, id);
}

void augmentShapefileWithUnboundedScores(const std::string filename, const std::vector<std::string> &score_list){
  auto gc = complib::ReadShapefile(filename);
  complib::CalculateListOfUnboundedScores(gc, score_list);
  complib::WriteShapeScores(gc, filename);
}

void addUnboundedScoresToNewShapefile(const std::string in_filename, const std::string out_filename, const std::vector<std::string> &score_list){
  auto gc = complib::ReadShapefile(in_filename);
  complib::CalculateListOfUnboundedScores(gc, score_list);
  complib::WriteShapefile(gc,out_filename);
}


std::string getBoundedScoresForGeoJSON(
  const std::string &gj_subunit,
  const std::string &gj_superunit,
  const std::string id,
  const std::string join_on,
  const std::vector<std::string> &score_list
){
  auto gc_sub = complib::ReadGeoJSON(gj_subunit);
  auto gc_sup = complib::ReadGeoJSON(gj_superunit);
  complib::CalculateListOfBoundedScores(gc_sub, gc_sup, join_on, score_list);
  return complib::OutScoreJSON(gc_sub, id);
}

void augmentShapefileWithBoundedScores(
  const std::string subunit_filename,
  const std::string superunit_filename,
  const std::string join_on,
  const std::vector<std::string> &score_list
){
  auto gc_sub = complib::ReadShapefile(subunit_filename);
  auto gc_sup = complib::ReadShapefile(superunit_filename);
  complib::CalculateListOfBoundedScores(gc_sub, gc_sup, join_on, score_list);
  complib::CalculateListOfUnboundedScores(gc_sub, score_list);
  complib::WriteShapeScores(gc_sub, subunit_filename);
}

void addBoundedScoresToNewShapefile(
  const std::string in_subunit_filename,
  const std::string in_superunit_filename,
  const std::string out_filename,
  const std::string join_on,
  const std::vector<std::string> &score_list
){
  auto gc_sub = complib::ReadShapefile(in_subunit_filename);
  auto gc_sup = complib::ReadShapefile(in_superunit_filename);
  complib::CalculateListOfBoundedScores(gc_sub, gc_sup, join_on, score_list);
  complib::CalculateListOfUnboundedScores(gc_sub, score_list);
  complib::WriteShapefile(gc_sub,out_filename);
}

PYBIND11_PLUGIN(_mander) {
  py::module m("_mander", "Internal library used by python-mander to calculate scores");

  m.def(
    "prepGeoJSON",
    &complib::PrepGeoJSON,
    "Load GeoJSON into memory for quick retrieval later."
  );

  m.def(
    "getListOfUnboundedScores",
    &complib::getListOfUnboundedScores,
    "Returns a list of unbounded compactness scores."
  );

  m.def(
    "getListOfBoundedScores",
    &complib::getListOfBoundedScores,
    "Returns a list of bounded compactness scores."
  );

  m.def(
    "getUnboundedScoresForGeoJSON",
    &getUnboundedScoresForGeoJSON,
    "Takes a GeoJSON string as input, calculates all scores, return a JSON dictionary of the scores keyed to values identified 'id' which are expected to be properties of the GeoJSON objects. If id='', then the object's 0-indexed order is used.",
    py::arg("geojson"),
    py::arg("id")="",
    py::arg("score_list")=""
  );

  m.def(
    "getBoundedScoresForGeoJSON",
    &getBoundedScoresForGeoJSON,
    "Takes a GeoJSON string as input, calculates all scores, return a JSON dictionary of the scores keyed to values identified 'id' which are expected to be properties of the GeoJSON objects. If id='', then the object's 0-indexed order is used.",
    py::arg("gj_subunit"),
    py::arg("gj_superunit"),
    py::arg("join_on")="",
    py::arg("join_id")="",
    py::arg("score_list")=""
  );

  m.def(
    "augmentShapefileWithBoundedScores",
    &augmentShapefileWithBoundedScores,
    "Given the filename of a shapefile containing subunits, and another of superunits, this function calculates the scores of its shapes and adds them to the file.",
    py::arg("subunit_filename"),
    py::arg("superunit_filename"),
    py::arg("join_id")="",
    py::arg("score_list")=""
  );

  m.def(
    "addBoundedScoresToNewShapefile",
    &addBoundedScoresToNewShapefile,
    "Reads a shapefile, calculates its scores, and outputs a new shapefile.",
    py::arg("in_subunit_filename")="",
    py::arg("in_superunit_filename")="",
    py::arg("out_filename")="",
    py::arg("join_on")="",
    py::arg("score_list")=""
  );

  return m.ptr();
}