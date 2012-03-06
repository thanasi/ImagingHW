# Athanasios Athanassiadis Feb 2012
from circhough import *
from scipy.misc import imread
from pylab import cm, imsave

im = imread('img_hough_circle.tif')
ht = hough(im/255.,38)

thresh = 75
im_inv = hough(ht>thresh,38)

imsave('hough_t.png', ht, cmap = cm.copper)
imsave('inverse_hough.png',5*im_inv+im/255, cmap=cm.spectral)