from tkinter import *

from IPython.display import display
import ipywidgets as widgets

import gmaps
 

import gmaps
import gmaps.datasets
import ipywidgets as widgets
import geopy
import gmaps.geojson_geometries
# export GOOGLE_API_KEY='AIzaSyBcT_KzlYcyYf-171L7pR6ngBgZHYq24C4'
window = Tk()




gmaps.configure(api_key = '')

fig = gmaps.figure(map_type='SATELLITE')

# generate some (latitude, longitude) pairs
locations = [(51.5, 0.1), (51.7, 0.2), (51.4, -0.2), (51.49, 0.1)]

heatmap_layer = gmaps.heatmap_layer(locations)
fig.add_layer(heatmap_layer)
fig
fig = gmaps.figure()
fig.add_layer(gmaps.heatmap_layer(locations))
fig


 

 
window.title("Welcome to LikeGeeks app")
 
lbl = Label(window, text=fig)
 
lbl.grid(column=0, row=0)
 
window.mainloop()