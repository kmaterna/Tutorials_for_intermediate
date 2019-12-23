# Color bar examples

import pygmt

# Concepts: Colorbar placement, text labels, bounding box, triangles, units, intensity. 
min_vert=0
max_vert=10
label_interval=2;
pygmt.makecpt(C="jet",T=str(min_vert-0.1)+"/"+str(max_vert+0.1)+"/0.1",H="mycpt.cpt");

fig = pygmt.Figure();
fig.coast(region=[-122.8, -121.8, 37.2, 38.2], projection="M8i",B="0.25",shorelines="0.5p,black",G='peachpuff2',S='skyblue',D="h");
# Horizontal color bar below the map borders
fig.colorbar(D="JBC+4.0i+h",C="mycpt.cpt",G=str(min_vert)+"/"+str(max_vert),B=["x"+str(label_interval),"y+L\"Disp (mm)\""]);  
# Horizontal color bar within the map borders
fig.colorbar(D="jBr+w2.5i/0.2i+o3.5c/1.5c+h",C="mycpt.cpt",I="0.8",G=str(min_vert)+"/"+str(max_vert),B=["x"+str(label_interval),"y+L\"Disp (mm)\""]); 
# Vertical color bar with background box
fig.colorbar(D="n0.06/0.045+w4.0i+e+v",C="mycpt.cpt",G=str(min_vert)+"/"+str(max_vert),
    F='+c0.4/1.3/0.4/0.4+ggray85+p0.5p,black+r10p',B=["x"+str(label_interval)+"+umm","y+LDisp"]);
fig.savefig('colorbar_examples.png');


