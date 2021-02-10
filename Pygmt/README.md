# Tutorials_for_intermediate

This repository holds examples, tutorials, and toy problems for learning intermediate topics in geophysical data analysis. One example is the new pygmt interface with GMT6 and Python3.6+. 

### Tool 1: Pygmt ###
#### Pygmt mapping can: ####
* Download topography using GMT6 capabilities and plot with grdimage (may only work when connected to Internet?)
* Add illumination with one command! (-I+d)
* Provide the familiar annotations using GMT syntax
* Place scale bar, legend, and color bar using geographic coordinates, justified, and normalized coordinates
* Label the color bar differently on x and y axes
* Make legends similar to GMT legends
* Save the map as a PNG or other formats

Example map built in Python using pygmt (code included): 


![Americas](https://github.com/kmaterna/Tutorials_for_intermediate/blob/master/Pygmt/pngs/CSA_gnss_figure.png)

![colorbars](https://github.com/kmaterna/Tutorials_for_intermediate/blob/master/Pygmt/pngs/colorbar_examples.png)

### Tool 2: GMT6 ###
An example of GMT6 modern mode vector graphing: 
See 'gmt6_vector.sh' for code.
```
# Example for vectors in GMT6 Modern Mode
# 'plot' creates the vector with -Sv[size]
# size denotes the size of the vector head (can also be passed from the input table)
# -W is the pen for the vector line
# +a is the angle of the vector head
# +h0 means no indent in the back of the vector head
# +p is the pen for the vector head
# +z means the vector is cartesian (convenient for mm/yr)

gmt begin vector_map png
myrange='-125/-121/38/42'
myproj='M3i'
gmt pscoast -R$myrange -J$myproj -Slightblue -B1.0 -Wthin,black
echo "-123 40.0" | gmt plot -Sc0.1 -Gred -Wthick,black
echo "-122.8 40.2" | gmt plot -Sc0.1 -Gred -Wthick,black
echo "-123 40.0 135 1.0" | gmt plot -Sv0.3+e+a50+gplum+h0+p0.4p,black -W1p,black  # an example vector, degrees CCW from east
echo "-122.8 40.2 -10 15" | gmt plot -Sv0.2+e+a50+gblack+h0+p1p,black+z0.1 -W1p,black  # an example vector, cartesian
gmt end
```

![vectors](https://github.com/kmaterna/Tutorials_for_intermediate/blob/master/Pygmt/pngs/vector_map.png)
