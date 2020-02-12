import json
import pandas as pd
import gmplot
import csv
import os

#Path of Location history Json File downloaded from google hangout
url = 'C:\\Users\\username\\takeout-201\\Takeout\\LocationHistory\\lh.json'

#Plot the Base map
gmap = gmplot.GoogleMapPlotter(14.35426, 78.1477, 7)

#Load the json file
with open(url) as f:
    data = json.load(f)

# select the column which hold the location data
df = pd.json_normalize(data['locations'])

# If the number of entries in Json is more the created map will freeze in browser to avoid it limit record
df = df.head(10000)

#Convert the lat and lang entries understandable by gmplot
df['latitudeE7'] = df['latitudeE7']/10000000
df['longitudeE7'] = df['longitudeE7']/10000000

#Assign Lat lang values to a list
latitudeE7 = df['latitudeE7'].tolist()
longitudeE7 = df['longitudeE7'].tolist()

# create the map with values of lat and lang
gmap.heatmap(latitudeE7, longitudeE7)
gmap.scatter(latitudeE7, longitudeE7, c='r', marker=True)

#save into an html file
gmap.draw("C:\\Users\\bharathkumar.akki\\Desktop\\gmap.html")
