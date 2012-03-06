# Athanasios Athanassiadis March 2012
import os
import numpy as np
from numpy.linalg import eig
from scipy.misc import imread, imsave

cov = np.cov

def arr2vec(arr, m=0):
    # flatten an n-dim array (arr) into a single vector with mean m
    return arr.flatten() - arr.mean()
    
def load_faces(folder):
    '''
    load_faces
            load a set of faces from a folder of tif images
            and return reduced set of faces with shape info
    '''
    
    filelist = np.array(os.listdir(folder))
    acceptable = ['.tif', '.tiff', '.png', '.jpg']
    
    # clean filelist
    keep = np.zeros(len(filelist), dtype=bool)
    for ext in acceptable:
        keep += (np.char.find(filelist, ext) >= 0)
    
    # load in files
    imarr = []
    for file_ in filelist[keep]:
        imarr.append(imread(os.path.join(folder,file_)).astype(np.float32))
    
    # create single 2D matrix out of images
    # with each image reduced to a column vector
    imarr2 = np.array([arr2vec(im) for im in imarr]).T
    
    # assume all ims are same shape to make life easier
    imshape = imarr[0].shape
    
    return imarr2, imshape
    
def eigenfaces(imarr, n=None):
    '''
    eigenfaces
        returns the first n eigenfaces calculated from an array of faces
        which has been reduced to 2D
        
        eigenfaces are the eigenvectors of the covariance matrix of the
        faces matrix
        
        this computation is simplified using the Turk-Pentland Trick
    
    '''
    
    C = cov(imarr.T)
    
    eigvals, eigvecs = eig(C)
        
    eigfaces = np.dot(imarr, eigvecs).T
    
    if n is None or n>len(eigfaces):
        n = len(eigfaces)
           
    return eigfaces[:n]
    
def approxiface(face, eigfaces, n=None):
    '''
    approxiface
        approximate a face based on eigfaces
        return first n approximations
    
    '''    
    
    if n is None or n>len(eigfaces):
        n = len(eigfaces)
    
    approxes = []
    
    for i in range(n):
        approxes.append(face * eigfaces[i])
        
    return approxes
