# pygmt_segfault 
# This produces a segmentation fault
# The G option in colorbar, when given the same argument twice, produces a segmentation fault. 

# This makes a seg fault. 

min_vert=0
max_vert=0
c_ntv = 0.1
label_interval=0.2;
pygmt.makecpt(C="jet",T=str(min_vert-0.1)+"/"+str(max_vert+0.1)+"/"+str(c_ntv),H="mycpt_faulty.cpt");

fig = pygmt.Figure();
fig.coast(region=[-122.9, -121.9, 37.2, 38.2], projection="M8i",B="0.25",shorelines="0.5p,black",G='peachpuff2',S='skyblue',D="h");
fig.colorbar(D="JBC+w4.0i+h",C="mycpt.cpt",G=str(min_vert)+"/"+str(max_vert),B=["x"+str(label_interval),"y+LVert(mm)"]);  # this is where the seg fault happens
fig.savefig('map.png');


