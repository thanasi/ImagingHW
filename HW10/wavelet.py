# Athanasios Athanassiadis February 2012
import numpy as np
import pywt
def haar_decompose(im,n=2):
    '''
    haar_decompose(im,n)
        Haar wavelet decomposition of an image
         using the Python Wavelet Transform (pywt) library
        
        im  :   source image
        n   :   number of iterations (req: 2**n <= min(im.shape))
    
    ''' 
    if n==0:
        return im
   
    shape = np.array(im.shape)		
    
    # make sure that the haar image has an even number of samples in each dir
    im_haar = np.zeros(2 * (shape / 2))
    
    # cap the max of n
    n = min(n,np.log2(min(shape)))
    
    # calculate coefficients of Haar wavelet transform
    cA, (cH, cV, cD) = pywt.dwt2(im,'haar')
        
    # fill harr image from top right corner:
    im_haar[:shape[0]/2,shape[1]/2:] = cV
    im_haar[shape[0]/2:,shape[1]/2:] = cD
    im_haar[shape[0]/2:,:shape[1]/2] = cH
    
    # if there are more iterations to perform, then do them
    # otherwise we're done
    if n>1:
        im_haar[:shape[0]/2,:shape[1]/2] = haar_decompose(cA, n-1)
    else:
        im_haar[:shape[0]/2,:shape[0]/2] = cA
    
    return im_haar   
    
