#!/bin/bash

# Example for vectors in GMT6 Modern Mode
# 'plot' does the vector with -Sv[size]
# size denotes the size of the vector head (can also be passed from the input table)
# -W is the pen for the vector line
# +a is the angle of the vector head
# +h0 means no indent in the back of the vector head
# +p is the pen for the vector head
# +z means the vector is cartesian (convenient for mm/yr)

gmt begin map
myrange='-125/-121/38/42'
myproj='M3i'
gmt pscoast -R$myrange -J$myproj -Slightblue -B1.0 -Wthin,black
echo "-123 40.0" | gmt plot -Sc0.1 -Gred -Wthick,black
echo "-122.8 40.2" | gmt plot -Sc0.1 -Gred -Wthick,black
echo "-123 40.0 135 1.0" | gmt plot -Sv0.3+e+a50+gplum+h0+p0.4p,black -W1p,black  # an example vector, degrees CCW from east
echo "-122.8 40.2 -10 15" | gmt plot -Sv0.2+e+a50+gblack+h0+p1p,black+z0.1 -W1p,black  # an example vector, cartesian
gmt end
