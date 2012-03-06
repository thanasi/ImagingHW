#Athanasios Athanassiadis Feb 2012
import numpy as np
inf = np.inf

#pad image with zeros    
def pad_image(im, pad=1):
    newim = np.zeros(np.array(im.shape) + 2*pad)
    newim[pad:-pad,pad:-pad] = im.copy()
    
    return newim

#compute the distance transform of a binary image
def dist_t(im):
    #make a binary copy, thresholding at 0
    #make anything inside of the region infinity for the forward pass
    dmap = 1.0 * (pad_image(im) > 0)
    dmap[dmap==1] = inf
    
    #first pass (forward)
    for i in range(1,im.shape[0]):
        for j in range(1,im.shape[1]):
            dmap[i,j] = min(dmap[i,j],dmap[i-1,j]+1,dmap[i,j-1]+1)
            
    #second pass (reverse)
    for i in range(1,im.shape[0]+1)[::-1]:
        for j in range(1,im.shape[1]+1)[::-1]:
            dmap[i,j] = min(dmap[i,j],dmap[i+1,j]+1,dmap[i,j+1]+1)
            
    #remove padding
    return dmap[1:-1,1:-1]