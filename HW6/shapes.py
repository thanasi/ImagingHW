# Athanasios Athanassiadis Feb 2012
import numpy as np

# calculate the (p,q)-moments of an image
# for p and q in range(n)
# x and y are reversed to account for row-col indexing
def get_moments(im, n):
	# initialize moments matrix
    M = np.zeros((n,n))
	
	# get list of pixels that are on and separate into list of x and y values
    pixlist = np.array(np.nonzero(im))
    y,x = pixlist
	
	# get the values at those points
    imvals = 1.0 * im[zip(pixlist)][0]
    N = len(imvals)
    if N==0:
        print 'get_moments: No figure found!'
        return []
		
	# CoM calculation
    y0,x0 = (pixlist * imvals).sum(1) / im.sum()
    
	# calculate all desired moments
    for p in range(n):
        for q in range(n):
            M[p,q] = ((x-x0)**p * (y-y0)**q * imvals).sum()
    
    return M,(x0,y0)
