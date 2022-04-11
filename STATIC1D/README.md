# STATIC1D Notes for Usage

March 2021, MacBook MacOS Mojave

### Step 1: Compile executables from source code. 

A fortran compiler is necsessary. 

**Kathryn's 2018 solution:** 

* Download iFort from Intel somehow, requiring a username and password. I don't remember how I did it. 
* change ```FFLAGS -mp``` into ```FFLAGS -fltconsistency``` in Makefile
* make all
```
FC=ifort
FFLAGS=-O2 -ftz -ip -ipo -axP -fltconsistency -align all -extend_source
```

**Kathryn's 2021 solution:**  

Error: my iFort license has expired and Intel has possibly discontinued the program. 
I will not solve this problem and will instead use the executables from 2018.  
I'm not sure how to solve this problem generally on a modern machine. 
This is only a problem if you move to a new machine or if you want to uncomment the line that calculates Bouguer gravity anomaly
in the stat0A.f source code. For static displacement only, I don't think it matters. 

### Step 2: Get happy Earth Structure
Establish earth structure in file earth.model_stat. 
The format of this file is: 

radius radius density bulk-modulus (10^10 Pa), shear-modulus (10^10 Pa), viscosity (n/a for static1d)
```
69 2  6371.000     2.214
 3300.000 3400.000   10.000   65.000    0.500 1.000000E+03
 3400.000 3480.000   10.000   65.000    0.500 1.000000E+03
 3480.000 3500.000    5.566   64.120   28.990 1.000000E+03
...
 6365.000 6367.000    2.600    5.200    2.660 0.100000E+12
 6367.000 6369.000    2.600    4.875    2.490 0.100000E+12
 6369.000 6371.000    2.600    4.875    2.490 0.100000E+12
```


### Step 3: Call stat0A for Green's Functions with given Earth structure
```bash
nice stat0A << ! > /dev/null
1 150
50.5 0.0
0.
!
```
I call this from an experiment directory (not the directory of the source code) that contains earth model file. The code will search for 'earth.model'
* Call stat0A code with a bash script.
    * 1 150: spherical harmonic degree
    * 50.5 0: lower_km upper_km depths to which input faults are specified
    * 0: calculting the static response at the surface
* Output: stat0.out, a binary file
* For 150 spherical harmonic degrees, it takes 5 seconds and generates 1.3Mb
* For 5000 spherical harmonic degrees, it takes 30 seconds and generates 41Mb


### Step 4: Static deformation, stat2gA version
```
nice stat2gA < stat2g.in_onefault > /dev/null
mv stat2g.out stat2g.out_onefault
```

##### Inputs: ```stat2g.in_onefault```
```
30.0 0.0  18.
1
14.0149100 93.5536400 162.5  24.0 139. 1000.
1600
     0.000000    87.000000
     0.000000    87.461540
     0.000000    87.923080
     0.000000    88.384613
     0.000000    88.846153
```
* 30 and 0     : Lower and upper edges of fault segment (km)
* 18           : Dip of fault (degrees)
* 1            : probably refers to 1 fault segment in the following 1 line
* 162.5        : fault length (km)
* 24.0         : fault strike (degrees CW from north)
* 139\.        : rake
* 1000         : fault slip (cm)
* (14.01, 93.55) : the latitude/longitude of the lower edge of the fault plane closest to the strike direction (ex: the lower northeast corner if the strike is 24 degrees).
* (0.0, 87.0) etc  : the latitude/longitude of points being evaluated at 1600 points

##### Outputs: 
Output displacements in the text file are in cm, in the same lon/lat order as the points in the input  file. 
* xdisp = columns[20:33]
* ydisp = columns[33:46]
* zdisp = columns[46:59]

### Step 4: Static deformation, stat2A version
stat2A goes looking for points in "./latlon.inDEF".
``` 
cp $pts_file latlon.inDEF
nice stat2A < stat2.in304 > /dev/null
mv stat2.out stat2.out304
```
##### Inputs: ```stat2.in304```
```
   20.0000000       0.00000000       35.0000000    
          17
   40.8810043      -123.631165       3.71262550      -23.6977844       90.0000000       1.00000000    
   40.9117355      -123.648262       3.71236300      -23.6977844       90.0000000       1.00000000    
   41.0173416      -123.754295       4.47418976      -44.5331955       90.0000000       1.00000000    
   41.0390663      -123.779137       4.63768196      -41.6477127       90.0000000       1.00000000 
```
* Cannot have a header line up top
* 20 0 : Lower and Upper edges of the fault plane 
* 35 : fault dip
* 17 : number of fault patches to follow
* 40.8810043      -123.631165 : lat, lon
* 3.71262550      -23.6977844 : length (km), strike (degrees CW from north)
* 90.0000000 : rake
* 1.00000000 : slip (cm)

##### Outputs: ```stat2.in304```
Output displacements in the text file are in cm, in the same lon/lat order as the points in the input  file. 
* xdisp = columns[20:33]
* ydisp = columns[33:46]
* zdisp = columns[46:59]

## Visualizing 
I use a few scripts for visualizing the earth model, fault trace, and Green's functions
