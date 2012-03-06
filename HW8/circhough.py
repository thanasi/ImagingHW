# Athanasios Athanassiadis Feb 2012
import numpy as np
from ball import make_ball

def hough(im, R):
    '''
     return Hough transform of a binary image containing circles of radius R
     the axes in the Hough transform represent the a and b center coords
     of a circle given by the equation:
        
        (x - a)**2 + (y - b)**2 = R**2
        
     for each 'on' point, p0, in the binary image, the set of centers of 
     circles that could pass through p0 is represented by a circle of 
     radius R about p0.  Therefore, for each 'on' point in the image, p0, 
     I will add a circle of radius R centered at p0 to the accumulator

    '''
    circ = make_ball(R,shell=1,bgsize=(2*R+1,2*R+1)).astype(int)
    # create accumulator with shape of image since we can only vary the centers
    L,W = im.shape
    acc = np.zeros(im.shape)
    for i in range(L):
        for j in range(W):
            if im[i,j]==1:
                # if near the edges, appropriately crop the circle
                if i<R:
                    i_min = 0
                    crop_top = R - i
                    i_max = i + R
                    crop_bottom = 2 * R
                elif i>L-R:
                    i_min = i - R
                    crop_top = 0
                    i_max = L
                    crop_bottom = L - 1 - i - R
                else:
                    i_min = i - R
                    crop_top = 0
                    i_max = i + R
                    crop_bottom = 2 * R
                
                if j<R:
                    j_min = 0
                    crop_left = R - j
                    j_max = j + R
                    crop_right = 2 * R
                elif j>W-R:
                    j_min = j - R
                    crop_left = 0
                    j_max = W
                    crop_right = W - 1 - j - R
                else:
                    j_min = j - R
                    crop_left = 0
                    j_max = j + R
                    crop_right = 2 * R
                
                # add circle centered at i,j to accumulator
                acc[i_min:i_max,j_min:j_max] += circ[crop_top:crop_bottom,
                                                     crop_left:crop_right]
                                                     
    return acc
