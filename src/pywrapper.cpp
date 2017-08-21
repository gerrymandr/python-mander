#include <compactnesslib.hpp>
#include <pybind11.h>

namespace py = pybind11;

//Tutorials
//http://www.benjack.io/2017/06/12/python-cpp-tests.html
//https://pybind11.readthedocs.io/en/stable/classes.html
//http://people.duke.edu/~ccc14/sta-663-2016/18G_C++_Python_pybind11.html

std::vector<std::string> getListOfScores() {
  return complib::score_names;
}

std::string getScoresForGeoJSON(const std::string &geojson, const std::string id, const std::vector<std::string> &score_list){
  auto gc = complib::ReadGeoJSON(geojson);
  complib::CalculateListOfScores(gc, score_list);
  return complib::OutScoreJSON(gc, id);
}

void augmentShapefileWithScores(const std::string filename, const std::vector<std::string> &score_list){
  auto gc = complib::ReadShapefile(filename);
  complib::CalculateListOfScores(gc, score_list);
  complib::WriteShapeScores(gc, filename);
}

void addScoresToNewShapefile(const std::string in_filename, const std::string out_filename, const std::vector<std::string> &score_list){
  auto gc = complib::ReadShapefile(in_filename);
  complib::CalculateListOfScores(gc, score_list);
  complib::WriteShapefile(gc,out_filename);
}



PYBIND11_PLUGIN(_mander) {
  py::module m("_mander", "Internal library used by python-mander to calculate scores");

  m.def(
    "getScoresForGeoJSON",
    &getScoresForGeoJSON,
    "Takes a GeoJSON string as input, calculates all scores, return a JSON dictionary of the scores keyed to values identified 'id' which are expected to be properties of the GeoJSON objects. If id='', then the object's 0-indexed order is used.",
    py::arg("geojson"),
    py::arg("id")=""
    py::arg("score_list")=""
  );

  m.def(
    "augmentShapefileWithScores",
    &augmentShapefileWithScores,
    "Given the filename of a shapefile, this function calculates the scores of its shapes and adds them to the file.",
    py::arg("filename"),
    py::arg("score_list")=""
  );

  m.def(
    "addScoresToNewShapefile",
    &addScoresToNewShapefile,
    "Reads a shapefile, calculates its scores, and outputs a new shapefile.",
    py::arg("in_filename"),
    py::arg("out_filename"),
    py::arg("score_list")=""
  );

  return m.ptr();
}