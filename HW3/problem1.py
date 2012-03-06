#Athanasios Athanassiadis Jan 2012
from segmentation import *

fig1 = np.fromfile('figure1_problem_set_3',dtype='>i2').reshape((192,161)) / 255.0
edge, chain = track_edge(fig1)
chain8 = reduce_edge(chain)
edge2 = decode_edge8(chain8, (192,161))

imsave('3-1a.png',fig1)
imsave('3-1b.png',(fig1-edge,fig1,fig1-edge))
imsave('3-1c.png',(fig1-edge2,fig1-edge2,fig1))
imsave('3-1d.png',(edge,edge2,edge2))

write_chain('problem1chain4.txt',chain)
write_chain('problem1chain8.txt',chain8)

#get and write perimiters
#for a chain of directions of length n,
#the perimeter length will be (n-2)+1
#because the first two 2 entries are start pix coords
#and it only takes (m-1) moves to traverse m pixels
with open('problem1.txt','w') as of:
    of.write('4-perim: {}px\n8-perim: {}px'.format(len(chain[2:]+1),len(chain8[2:]+1)))