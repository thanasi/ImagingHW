# Athanasios Athanassiadis March 2012
import os
import numpy as np
from numpy.linalg import eig
from scipy.misc import imread, imsave


cov = np.cov

def load_faces(folder):
    '''
    load_faces
            load a set of faces from a folder of tif images
            and return reduced set of faces with shape info
    '''
    
    filelist = os.listdir(folder)

    origfaces = []
    for fn in filelist:
        origfaces.append(
            imread(os.path.join(folder,fn)))

    origfaces = np.array(origfaces, dtype=np.int16)

    avgface = origfaces.sum(0) / origfaces.shape[0]
    shape = avgface.shape

    faces = np.array([(face-avgface).flatten() for face in origfaces]).T

            
    return origfaces, faces, shape
    
def eigenfaces(faces, n=None):
    '''
    eigenfaces
        returns the first n eigenfaces calculated from an array of faces
        which has been reduced to 2D
        
        eigenfaces are the eigenvectors of the covariance matrix of the
        faces matrix
        
        this computation is simplified using the Turk-Pentland Trick
    
    '''
    
    C = cov(faces.T)
        
    eigvals, eigvecs = eig(C)

    eigfaces = np.dot(faces, eigvecs).T
    
    # sort by eigenvalue
    eigzip = zip(eigvals, eigfaces)
    eigzip.sort(key = lambda x: x[0])
    
    eigfaces = np.array([pair[1] for pair in eigzip], dtype=np.int16)[::-1]
           
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
        weights.append( (eigfaces[i] * face.flatten()).sum() )
    
    # normalize weights
    weights = np.array(weights, dtype=np.float)
    weights /= np.sqrt((weights**2).sum())
    
    approxes = np.zeros((n,face.flatten().shape[0]))

    for i in range(n):
        approxes[i] = approxes.sum(0) + weights[i] * eigfaces[i]

    return approxes
