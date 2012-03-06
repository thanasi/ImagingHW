# Athanasios Athanassiadis Feb 2012
from shapes import *
from scipy.misc import imread,imsave

im = imread('img_moment.tif')
im *= 1.0/im.max()

M,CoM = get_moments(im, 3)
center = np.zeros(im.shape)
center[CoM[1],CoM[0]] = 1

imsave('img_moment.png', (im, im - center, im-center))
with open('moments.txt','w') as of_:
    of_.write('M00:\t{}\nM02:\t{}\nM20:\t{}'.format(M[0,0],M[0,2],M[2,0]))