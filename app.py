# importing all project related libraries
import ee
from ee import image
import folium
from folium import features
from folium import WmsTileLayer
import geemap
import os
import webbrowser

#################### Earth Engine Configuration #################### 
#ee.Authenticate()

# initializing the earth engine library
ee.Initialize()

# ##### earth-engine drawing method setup
def add_ee_layer(self, ee_image_object, vis_params, name):
  map_id_dict = ee.Image(ee_image_object).getMapId(vis_params)
  layer = folium.raster_layers.TileLayer(
      tiles = map_id_dict['tile_fetcher'].url_format,
      attr = 'Map Data &copy; <a href="https://earthengine.google.com/">Google Earth Engine</a>',
      name = name,
      overlay = True,
      control = True
  )
  layer.add_to(self)
  return layer

# configuring earth engine display rendering method in folium
folium.Map.add_ee_layer = add_ee_layer

#################### IMAGERY ANALYSIS ####################
aoi = ee.Geometry.Point([2.310362, 36.577489]).buffer(10500)

# ########## Elevation

# ##### JAXA DSM (Digital Surface Model) collection: 30m resolution
# Initializing the image collection
dem_i = ee.Image('JAXA/ALOS/AW3D30/V2_2').clip(aoi)
dem = dem_i.updateMask(dem_i.gt(0))
# Visual parameters for the DEM imagery
dem_params = {
  'min': 0,
  'max': 905,
  'bands': ['AVE_DSM']
}

# Deriving elevation from previous DEM
elevation = dem.select('AVE_DSM').clip(aoi)

# Visual parameters for the elevation imagery
elevation_params = {
  'min' : -5,
  'max' : 9000,
  'palette' : ['#053061', '#2166ac', '#4393c3', '#92c5de', '#d1e5f0', '#f7f7f7', '#fddbc7', '#f4a582', '#d6604d', '#b2182b', '#67001f'],
  'opacity': 0.8
}

# Deriving hillshades from the elevation layer
hillshade = ee.Terrain.hillshade(elevation)

# Visual parameters for hillshade layer
hillshade_params = {
  'min': 0,
  'max': 905,
  'palette': ['#000000', '#ffffff']
}

# Deriving slopes from the elevation layer
slopes = ee.Terrain.slope(elevation).clip(aoi)

# Visual parameters for the slopes imagery
slopes_params = {
  'min' : 0,
  'max' : 90,
  'palette' : ['#6f0a91','#43d1bf','#86ea50','#ccec5a'],
  'opacity': 0.8
}

# Deriving contour lines from the elevation layer
contours = geemap.create_contours(elevation, 0, 905, 20, region=aoi)

# Visual parameters for the contour lines
contours_params = {
  'min': 0,
  'max': 905,
  'palette': ['#053061', '#2166ac', '#4393c3', '#92c5de', '#d1e5f0', '#f7f7f7', '#fddbc7', '#f4a582', '#d6604d', '#b2182b', '#67001f'],
  'opacity': 0.3
}


#################### MAIN PROJECT MAP ####################
# setting up the main map for the project
m = folium.Map(location = [36.5711, 2.2834], tiles=None, zoom_start = 12, control_scale = True)

# ########## Primary basemaps (victor data):
basemap1 = folium.TileLayer('cartodbdark_matter', name='Dark Matter Basemap')
basemap1.add_to(m)

#################### COMPUTED RASTER LAYERS ####################

# # adding DSM layer
m.add_ee_layer(dem, dem_params, 'JAXA DSM 30m')

# # adding Hillshades
HILLSHADE = m.add_ee_layer(hillshade, hillshade_params, "Hillshade")

# # adding SRTM elevation layer
ELEVATION = m.add_ee_layer(elevation, elevation_params, 'Elevation')

# # adding slopes layer
SLOPES = m.add_ee_layer(slopes, slopes_params, 'Slopes')

# # adding contour lines to the map
CONTOURS = m.add_ee_layer(contours, contours_params, 'Contour lines')

# Layer controller 

folium.LayerControl(collapsed=False).add_to(m)

# Generating a file for the map and setting it to open on default browser
m.save('index.html')

# Opening the map file in default browser on execution
webbrowser.open('index.html')