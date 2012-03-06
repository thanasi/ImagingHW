# Athanasios Athanassiadis March 2012
import os
import numpy as np
from numpy.linalg import eig
from scipy.misc import imread, imsave


cov = np.cov

def contrast_adjust(im):
    retim = im
    retim = im - im.min()
    retim *= 255.0/retim.max()
    return retim.astype(np.int32)

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
        imarr.append(
              imread(os.path.join(folder,file_))
              )
    
    imarr = contrast_adjust(np.array(imarr))
    avgface =  (imarr.sum(0) / len(imarr)).flatten()
    
    # create single 2D matrix out of images
    # with each image reduced to a column vector
    imarr2 = np.array([im.flatten()-avgface for im in imarr]).T
    
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

    # normalize eigenvectors    
    for i in range(len(eigvecs)):
        eigvecs[i] /= np.sqrt(np.sum(eigvecs[i]**2))

    eigfaces = np.dot(imarr, eigvecs).T
    
    # sort by eigenvalue
    eigzip = zip(eigvals, eigfaces)
    eigzip.sort(key = lambda x: x[0])
    
    eigfaces = np.array([contrast_adjust(pair[1]) for pair in eigzip[::-1]])
           
    if n is None or n>len(eigfaces):
        n = len(eigfaces)
        
    return eigfaces[:n]
    
def approxiface(face, eigfaces, n=None):
    '''
    approxiface
        approximate a face b,ased on eigfaces
        return first n approximations
    
    '''    
           
    if n is None or n>len(eigfaces):
        n = len(eigfaces)
    
    weights = []
    
    for i in range(n):
        weights.append((face * eigfaces[i]).sum())
    
    # normalize weights
    weights = np.array(weights, dtype=np.float)
    weights /= weights.sum()
    
    approxes = np.zeros((n,face.shape[0]))

    for i in range(n):
        approxes[i] = contrast_adjust(
            approxes.sum(0) + weights[i] * eigfaces[i].astype(np.float)
            )

    return approxes
