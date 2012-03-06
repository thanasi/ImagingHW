#Athanasios Athanassiadis Jan 2012
from preprocessing import *

im = load('figure_problem_set_2')
mags, dirs = edges(im, True)
im1,im2,im3 = edge_sobel(im)

imsave('2-2.png',im)
imsave('2-2a.png',mags)
imsave('2-2b.png',dirs)
imsave('2-2c.png',(im1*255./im1.max(),mags,im3*255./im3.max()))