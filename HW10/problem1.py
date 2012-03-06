# Athanasios Athanassiadis February 2012
from mywavelet import *
from scipy.misc import imread
from pylab import imsave, cm

im  = imread('img_lena.tif')

n = 2
im_haar = haar_decompose(im, n)

imsave('my_lena_haar_{}.png'.format(n), im_haar, cmap=cm.gray)
