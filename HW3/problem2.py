#Athanasios Athanassiadis Jan 2012
from segmentation import *
from ball import make_ball

fig1 = np.fromfile('figure1_problem_set_3',dtype='>i2').reshape((192,161))
fig1 /= 1.0*fig1.max()

#set a new starting point that is on the edge on the other side of the figure
i0,j0 = 71,80
startpoint = np.zeros(fig1.shape)
startpoint[i0,j0] = 1
edge, chain = track_edge(fig1,(i0,j0))
ball = make_ball(5,shell=1,center=(i0,j0),bgsize=(192,161))

#set up colors
r = fig1*(1-edge)*(1-ball)*(1-startpoint)+ball+startpoint
g = fig1*(1-edge)*(1-ball)*(1-startpoint)+startpoint
b = fig1*(1-ball)*(1-startpoint)
imsave('3-2a.png', (r,g,b))