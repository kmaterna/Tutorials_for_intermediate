# VISCO1D Notes for Usage

May 2021, MacBook MacOS Mojave.  

This tutorial is from my homemade experience calculating an interseismic backslip calculation over a fully-relaxed mantle 
with gravitational forces. Much of this will be duplicated from the VISCO1D tutorial.  

### Step 1: Compile executables from source code. 

A fortran compiler is necsessary (gfortran is fine). 'make all' .  

### Step 2A: Get happy Earth Structure
Establish earth structure in file earth.model.
```
23 3  3600.000     0.892
 6100.000 6129.000    3.402   15.000    7.000 0.100000E+12
 6129.000 6155.000    3.402   15.000    7.000 0.100000E+12
 6155.000 6180.000    3.393   15.000    7.000 4.000000E+01
 6180.000 6206.000    3.387   15.000    7.000 4.000000E+01
 6206.000 6231.000    3.379   15.000    7.000 4.000000E+01
 6231.000 6257.000    3.372   15.000    7.000 4.000000E+01
 ...
```

 
The first row is: N_total_layers, N_viscoelastic_layers, earth radius, DEPFAC

A smaller earth radius speeds up the calculation and doesn't make a difference if you're calculating over a small-ish region.

Eigenfunctions are evaluated from surface (depth = 0) to depth = 28 * DEPFAC km. 

Line Format for layers (assuming same as Static-1D): 

radius radius density bulk-modulus (10^10 Pa), shear-modulus (10^10 Pa), viscosity (number * 10^18 Pa-s; n/a for static1d)

In this case, we have a spherical shell of about 200 km thick, with the top 25 km being elastic, 
the next 186 km being viscoelastic, and then another 55 km of elastic at the bottom.  Not sure why.
The slip goes down to 28*0.892 km, which is 25 km.    

### Step 2B: Call visco1d scripts to generate decay functions
```bash
cp earth.modelWUS earth.model   # assumes you have earth.model in your directory
nice decay << ! > /dev/null
2 1000
!
nice vtordep << ! > /dev/null
0.
!

nice decay4m << ! > /dev/null
2 1000
!
nice vsphm << ! > /dev/null
0.
!

```
I call this from an experiment directory (not the directory of the source code) that contains earth model file.
* 2 1000 means... not sure. It's possible that 1000 is vmult. 

### Step 3: Call strainAp for deformation
```
cp latlon.inGPS latlon.inDEF

nice strainAp < strainAp.inOneFault > /dev/null
mv strainAp.out strainAp.outOneFault

```

##### Inputs:
```
Example fault (Mad River)
   20.0000000       0.00000000       35.0000000    
1900. 1900. 2000. 1000. 500.0
          17
   40.8810043      -123.631165       3.71262550      -23.6977844       90.0000000       500.0    
   40.9117355      -123.648262       3.71236300      -23.6977844       90.0000000       500.0    
   41.0173416      -123.754295       4.47418976      -44.5331955       90.0000000       500.0    
   41.0390663      -123.779137       4.63768196      -41.6477127       90.0000000       500.0    
   41.0702400      -123.815659       4.63671827      -41.6477127       90.0000000       500.0    
   41.0928574      -123.843666       2.57415223      -43.4000359       90.0000000       500.0
...
1
0    
```
* 20 and 0     : Lower and upper edges of fault segment (km)
* 35           : Dip of fault (degrees)
* 1900 1900 2000  : earthquake happened in 1900.  We evaluate displacements from year 1900 to year 2000.
* 1000         : vmult  (1000 is very high, so this basically simulates interseismic velocities)
* 500          : periodicity of earthquake cycle
* 17           : refers to 17 fault segments in the following 17 line
* faults       : lat, lon, length (km), strike (degrees CW from north), rake, slip (cm) 
* (40.8810043 -123.631165) : the latitude/longitude of the lower edge of the fault plane closest to the strike direction (ex: the lower northeast corner if the strike is 24 degrees).

I don't know what the 1/0 at the end represent.  

##### Outputs: 
Output displacements in the text file are in cm, in the same lon/lat order as the points in the input  file. 
* xdisp = columns[20:33]
* ydisp = columns[33:46]
* zdisp = columns[46:59]
