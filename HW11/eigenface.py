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
                
    origfaces = np.array(origfaces).astype(np.int16)

    avgface = origfaces.sum(0) / origfaces.shape[0]
    shape = avgface.shape

    faces = np.array([(face-avgface).flatten() for face in origfaces]).T

            
    return origfaces, faces, shape
    
def eigenfaces(faces, n=None):
    '''
    eigenfaces
        returns the first n eigenfaces (principal components)
        calculated from an array of face which has been reduced to 2D
        
        eigenfaces are the eigenvectors of the covariance matrix of the
        faces matrix
        
        this computation is simplified using the Turk-Pentland Trick
    
    '''
    
    C = cov(faces.T, bias=1)
        
    # columns in eigvecs represent individual eigenvectors
    # that correspond to each eigenval
    eigvals, eigvecs = eig(C)
    
    if n is None or n>len(eigvals):
        n = len(eigvals)
        
    # sort by eigenvalue (decreasing)
    # and transpose so rows contain eigenvectors
    eigzip = zip(eigvals, eigvecs.T)
    eigzip.sort(key = lambda x: x[0])
    eigenvecs_sorted = np.array([pair[1] for pair in eigzip[::-1]])
    
    eigfaces = np.zeros((n, faces.shape[0]))
    
    for l in range(n):
        for k in range(faces.shape[1]):
            eigfaces[l] += (eigvecs[l,k] * faces[:,k])
    
    return eigfaces.astype(np.int16)
    
def approxiface(face, eigfaces, avgface, n=None):
    '''
    approxiface
        approximate a face b,ased on eigfaces
        return first n approximations
    
    '''    

    if n is None or n>len(eigfaces):
        n = len(eigfaces)
        
    weights = np.zeros(n)
    
    for k in range(n):
        weights[k] = np.dot(eigfaces[k], face-avgface)
        
    weights /= np.sqrt((weights**2).sum())
    
    approxes = np.zeros((n, eigfaces.shape[1]))
    approxes[0] = weights[0] * eigfaces[0]
    for k in range(1,n):
        approxes[k] = approxes[k-1] + (weights[k] * eigfaces[k])
    
    return approxes
