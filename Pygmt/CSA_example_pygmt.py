"""
# Make a map in pygmt! This gives examples of how to use features. 
# Be sure you're in your pygmt activated environment
# K. Materna, December 2019
# 
# Features Used Here: 
# Add a title to the frame
# Download topography using GMT6 capabilities and plot with grdimage (may only work when connected to Internet?)
# Add illumination with one command! (-I+d)
# Add thick coastlines and borders every 5 degrees
# Place the scale bar using geographic coordinates
# Add thin country borders
# Color the water area lightblue
# Provide text labels for two countries
# Plot capital cities, major cities, and GNSS data locations
# Provide a labeled color bar for the default GMT color scale
# Restrict the color bar to a range that makes sense
# Place the color bar on the map with normalized coordinates
# Label the color bar differently on x and y axes
# Place a legend in bottom-left using "justified" coordinates
# Fill the legend with a fun color that exists in the GMT palette
# Save the map as a PNG
"""

import pygmt
import numpy as np 

region = [-87, -67, -2, 18]
proj = "M8i"
capital_cities_x = [-74.0721, -79.5199, -84.0907, -86.2362, -78.4678];
capital_cities_y = [4.7110, 8.9824, 9.9281, 12.1150, -0.1807];
major_cities_x = [-74.8070, -75.5742, -71.6125];
major_cities_y = [11.0041, 6.2486, 10.6427];
[gps_lon, gps_lat] = np.loadtxt("CSA_station_coords.txt",unpack=True, usecols=(0,1));

# Make figure
fig = pygmt.Figure()
fig.basemap(region=region,projection=proj,B="+t\"GNSS Stations in South and Central America\"")
fig.grdimage("@earth_relief_02m",region=region,I="+d");  # takes a little while the first time, but faster each time afterwards
fig.coast(shorelines="1.0p,black",region=region,projection=proj,L="g-71.5/0+c1.5+w200",B="5.0")
fig.coast(region=region,projection=proj,N='1',W='0.5p,black',S='lightblue')
fig.text(x=-71,y=3,text="Colombia",font='15p,Helvetica-Bold,black')
fig.text(x=-85.1,y=13,text="Nicaragua",font='15p,Helvetica-Bold,black')
fig.plot(x=capital_cities_x,y=capital_cities_y,S='a0.25i',G='red',W='0.5p,yellow')
fig.plot(x=major_cities_x,y=major_cities_y,S='c0.12i',G='red',W='1.0p,white')
fig.plot(x=gps_lon, y=gps_lat, S='i0.1i',G='royalblue2',W='thin,black')
fig.colorbar(D="n0.05/0.2+w4.0/0.5",G="0/4000",B=["x1000+um","y+LElevation"])
fig.legend(region=region, projection=proj,spec="legendfile.txt",D="jBL+o0.2c",F="+gantiquewhite+pthick,black");
fig.savefig('CSA_gnss_figure.png')


