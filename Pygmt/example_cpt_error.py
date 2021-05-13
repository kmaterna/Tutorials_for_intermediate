import pygmt

"""
Questions:
A single call to interpret a color from a CMAP doesn't work. 
The behavior is different for 
- single polygons (returns a signed number)
- single points (returns 0)
Neither is the desired behavior. 
In this single-call case, why does it require a string in the G argument?
The result is I can't figure out how to plot custom-colored polygons at all 
(usually I would just plot them as indivual calls to plot() ). 
Is there another way to plot polygons with cmap colors? 
"""

# Make CPT and Fake Data
pygmt.makecpt(C="jet",T="-1.0/1.0/0.05",H="mycpt.cpt");
xdata = [-123, -122.5, -122.0, -121.5]; 
ydata = [36.5, 37, 37.5, 38]; 
zdata = [-0.7, -0.25, 0.25, 0.7];

#  Batch Calling : works
fig = pygmt.Figure()
title="+t\"Batch to CMAP - Works for Points.\""; 
fig.coast(region=[-124, -120, 35, 39], projection="M7i", B=[title,"1.0"],shorelines="1.0p,black"); 
fig.colorbar(D="jBr+w3.5i/0.2i+o5.5c/1.5c+h",C="mycpt.cpt",I="0.8",G="-1.0/1.0",B=["x"+str(0.2),"y+L\"KPa\""]); 
fig.plot(x=xdata, y=ydata, color=zdata, style="c1.8c", pen="thick,black", C="mycpt.cpt"); 
fig.savefig("Working.png");

#  Single Calls Only : doesn't do the right thing
fig = pygmt.Figure()
title="+t\"Single Calls to CMAP.\""; 
fig.coast(region=[-124, -120, 35, 39],projection="M7i",shorelines="1.0p,black",B=[title,"1.0"]); 
fig.colorbar(D="jBr+w3.5i/0.2i+o5.5c/1.5c+h",C="mycpt.cpt",I="0.8",G="-1.0/1.0",B=["x"+str(0.2),"y+L\"KPa\""]); 
for i in range(len(xdata)):  # just looping through the data
	fig.plot(x=xdata[i], y=ydata[i], G=[zdata[i]], style="c1.8c", pen="thick,black", C="mycpt.cpt");  # plotting a point with associated cmap data
	xdata_long = [xdata[i]+0.2, xdata[i]+0.3, xdata[i]+0.3, xdata[i]+0.2, xdata[i]+0.2];  # building a polygon
	ydata_long = [ydata[i], ydata[i], ydata[i]+0.1, ydata[i]+0.1, ydata[i]];  # building a polygon
	fig.plot(x=xdata_long, y=ydata_long, G=str(zdata[i]), pen="thick,black", C="mycpt.cpt");  # plotting the polygon with associated cmap data
fig.savefig("Not_Working.png");
