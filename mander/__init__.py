import _mander

def prepGeoJSON(geojson):
  """Loads GeoJSON into the mander library for accelerate processing later.

     Parameters:
     geojson -- The GeoJSON to load

     Returns:
     A string that can be passed in lieu of the original GeoJSON to take
     advatange of internal processing that has already been done.
  """
  return _mander.prepGeoJSON(geojson)



def getListOfUnboundedScores():
  """Returns a list of scores the library can calculate.
     Subsets of this list may be passed to the other functions in the library.
     Scores listed are those which can be calculated purely using the shape
     of a single district.

     Returns:
     The list of unbounded scores.
  """
  return _mander.getListOfUnboundedScores()



def getListOfBoundedScores():
  """Returns a list of scores the library can calculate.
     Subsets of this list may be passed to the other functions in the library.
     Scores listed are those in which a superunit bounds a subunit.

     Returns:
     The list of bounded scores.
  """
  return _mander.getListOfBoundedScores()



def getUnboundedScoresForGeoJSON(geojson, id="", score_list=[]):
  """Calculates unbounded scores for a given GeoJSON string.

  Parameters:
  geojson    -- GeoJSON string for which to calculate scores.
                Can also use a string returned by prepGeoJSON()
  id         -- An attribute value used to key the JSON output
  score_list -- A list of scores to calculate. Valid values from
                `getListOfUnboundedScores()`
                An empty list indicates all scores should be calculated.

  Returns:
  A JSON dictionary whose keys are taken from `id` or are the 0-based index 
  number of the multipolygon for which the scores were calculated.
  """

  return _mander.getUnboundedScoresForGeoJSON(geojson,id,score_list)



def getBoundedScoresForGeoJSON(gj_sub, gj_sup, join_on, id="", score_list=[]):
  """Calculates unbounded scores for a given GeoJSON string.

  Parameters:
  gj_sub     -- GeoJSON string of subunit for which to calculate scores.
                Can also use a string returned by prepGeoJSON()
  gj_sup     -- GeoJSON string of a superunit which bounds the subunit.
                Can also use a string returned by prepGeoJSON()
  id         -- An attribute value used to key the JSON output. An empty string
                defaults to a number representing the order of the multipolygon
                within the GeoJSON.
  join_on    -- Attribute present in both sub-unit and super-unit used to match
                the two
  score_list -- A list of scores to calculate. Valid values from
                `getListOfUnboundedScores()` and `getListOfBoundedScores()`
                An empty list indicates all scores should be calculated.

  Returns:
  A JSON dictionary whose keys are taken from `id` or are the 0-based index 
  number of the multipolygon for which the scores were calculated.
  """

  return _mander.getScoresForGeoJSON(geojson,id,score_list)



def augmentShapefileWithUnboundedScores(filename, score_list=[]):
  """Adds indicated scores to an existing shapefile

  Parameters:
  filename   -- File to which scores should be added
  score_list -- A list of scores to calculate. Valid values from 
                `getListOfUnboundedScores()`
                An empty list indicates all scores should be calculated.

  Returns:
  No return. The file is modified or an exception is thrown.
  """

  return _mander.augmentShapefileWithUnboundedScores(filename,score_list)



def addUnboundedScoresToNewShapefile(in_filename, out_filename, score_list=[]):
  """Adds indicated scores to an existing shapefile

  Parameters:
  in_filename  -- File containing regions to be scored
  out_filename -- Filename of new shapefile which will contain the scores
  score_list   -- A list of scores to calculate. Valid values from 
                  `getListOfUnboundedScores()`
                  An empty list indicates all scores should be calculated.

  Returns:
  No return. The new shapefile is built or an exception is thrown.
  """

  return _mander.addUnboundedScoresToNewShapefile(in_filename,out_filename,score_list)



def augmentShapefileWithBoundedScores(sub_filename, sup_filename, join_on, score_list=[]):
  """Adds indicated scores to an existing shapefile

  Parameters:
  sub_filename  -- File containing the subunits
  sup_filename  -- File containing the superunits which bound the subunits
  join_on       -- Name of an attribute in both sub- and superunits which 
                   indicates nestedness
  score_list   -- A list of scores to calculate. Valid values from
                  `getListOfUnboundedScores()` or `getListOfBoundedScores()`
                  An empty list indicates all scores should be calculated.

  Returns:
  No return. The file is modified or an exception is thrown.
  """

  return _mander.augmentShapefileWithBoundedScores(sub_filename,sup_filename,join_on,score_list)



def addBoundedScoresToNewShapefile(sub_filename, sup_filename, out_filename, join_on, score_list=[]):
  """Adds indicated scores to an existing shapefile

  Parameters:
  sub_filename  -- File containing the subunits
  sup_filename  -- File containing the superunits which bound the subunits
  out_filename  -- Filename of output shapefile
  join_on       -- Name of an attribute in both sub- and superunits which 
                   indicates nestedness
  score_list   -- A list of scores to calculate. Valid values from
                  `getListOfUnboundedScores()` or `getListOfBoundedScores()`
                  An empty list indicates all scores should be calculated.

  Returns:
  No return. The new shapefile is built or an exception is thrown.
  """

  return _mander.addBoundedScoresToNewShapefile(sub_filename,sup_filename,out_filename,join_on,score_list)
