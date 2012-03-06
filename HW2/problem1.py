#Athanasios Athanassiadis Jan 2012
from preprocessing import *

im = load('figure_problem_set_2')

im_rot = rotate(im, 80)
im_rot2 = rotate(im, -52, interp='linear', reshape=True)

imsave('2-1.png', im)
imsave('2-1a.png',im_rot)
imsave('2-1b.png', im_rot2)
