# Athanasios Athanassiadis February 2012
import numpy as np
import pylab as pl

def haar_decompose(im_orig,n=2):
    '''
    haar_decompose(im,n)
        Haar wavelet decomposition of an image - this can be performed
        discretely by just calculating the sums and differences between
        neighboring samples, and passing the results recursively
        
    INPUTS:
        im  :   source image
        n   :   number of iterations (req: 2**n <= min(im.shape))
    
    '''
    im = im_orig.copy().astype(np.int64)
    if n==0:
        return im_orig
   
    shape = np.array(im.shape)		
    im_haar = np.zeros(2 * (shape / 2))
    
    # cap the max of n
    n = min(n,np.log2(min(shape)))
    
    # initialize first step images (for after horizontal transform)
    imLF = np.zeros((shape[0],shape[1]/2))
    imHF = np.zeros((shape[0],shape[1]/2))
    
    # initialize second step images (final quadrants)
    cA = np.zeros(shape/2)  # main image DC components
    cV = np.zeros(shape/2)  # vertical edge-enhanced
    cH = np.zeros(shape/2)  # horizontal edge-enhanced
    cD = np.zeros(shape/2)  # diagonal edge-enhanced
    
    # calculate 1D DWT horizontally ( & account for odd number of rows)
    for i in range(shape[0] - shape[0]%2):
        cL1,cH1 = harr1D(im[i,:])
        imLF[i,:] = cL1
        imHF[i,:] = cH1  
      
    # calculate 1D DWT vertically
    for j in range(shape[1]/2):
        cL2,cH2 = harr1D(imLF[:,j])
        cL3,cH3 = harr1D(imHF[:,j])
        
        # low freq of low freq is cA
        # high freq of low freq is cH
        # low freq of high freq is cV
        # high freq of high freq is cD
        cA[:,j] = cL2
        cH[:,j] = cH2
        cV[:,j] = cL3
        cD[:,j] = cH3       
    
    # fill harr image from top right corner, leaving recursion for the end
    im_haar[:shape[0]/2,shape[1]/2:] = cV
    im_haar[shape[0]/2:,shape[1]/2:] = cD
    im_haar[shape[0]/2:,:shape[1]/2] = cH
    im_haar[:shape[0]/2,:shape[1]/2] = haar_decompose(cA, n-1)

    return im_haar
 
def harr1D(sig):
    '''
    harr1d(sig)
        takes a 1D signal and returns its discrete Harr wavelet transform
        in the form of the high and low frequency components of the signal
    
    INPUTS
        sig :   input signal
    
    '''
    cL = np.zeros(len(sig)/2)
    cH = np.zeros(len(sig)/2)

    # takes sums/differences for HF and LF components, and normalize
    for i in range(len(sig)/2-1):
        cL[i] = 1.0 * (sig[2*i+1] + sig[2*i]) / np.sqrt(2)
        cH[i] = 1.0 * (sig[2*i+1] - sig[2*i]) / np.sqrt(2)
    
    
    return cL,cH
