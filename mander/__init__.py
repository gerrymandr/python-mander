import _mander


def getListOfScores():
  """Returns a list of scores the library can calculate.
     Subsets of this list may be passed to the other functions in the library.
  """
  return _mander.getListOfScores()



def getScoresForGeoJSON(geojson, id="", score_list=[]):
  """Calculates scores for a given GeoJSON string.

  Parameters:
  geojson    -- GeoJSON string for which to calculate scores.
  id         -- An attribute value used to key the JSON output
  score_list -- A list of scores to calculate. Valid values from `getListOfScores()`
                An empty list indicates all scores should be calculated.

  Returns:
  A JSON dictionary whose keys are taken from `id` or are the 0-based index 
  number of the multipolygon for which the scores were calculated.
  """

  return _mander.getScoresForGeoJSON(geojson,id,score_list)



def augmentShapefileWithScores(filename, score_list=[]):
  """Adds indicated scores to an existing shapefile

  Parameters:
  filename   -- File to which scores should be added
  score_list -- A list of scores to calculate. Valid values from `getListOfScores()`
                An empty list indicates all scores should be calculated.

  Returns:
  No return. The file is modified or an exception is thrown.
  """

  return _mander.augmentShapefileWithScores(filename,score_list)



def addScoresToNewShapefile(in_filename, out_filename, score_list=[]):
  """Adds indicated scores to an existing shapefile

  Parameters:
  in_filename  -- File to which scores should be added
  out_filename -- Filename of new shapefile which will contain the scores
  score_list   -- A list of scores to calculate. Valid values from `getListOfScores()`
                  An empty list indicates all scores should be calculated.

  Returns:
  No return. The new shapefile is built or an exception is thrown.
  """

  return _mander.addScoresToNewShapefile(in_filename,out_filename,score_list)
