#Athanasios Athanassiadis Feb 2012
from scipy.misc import imread, imsave
from distT import *

im = imread('img_distance.tif')
im *= 1.0 / im.max()
dmap = dist_t(im)

im *= 1.0 * dmap.max()
imsave('5-1a.png',dmap)
imsave('5-1b.png',(im,im-dmap,im))