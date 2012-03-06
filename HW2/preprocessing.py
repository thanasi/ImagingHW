#Athanasios Athanassiadis Jan 2012
import numpy as np
from scipy.misc import imsave
from scipy.ndimage import convolve
from ball import eight_dist

sin = np.sin
cos = np.cos
atan2 = np.arctan2

#####Image Loading##############################################################
def load(filename, shape=(256,256), d='>i2'):
    im = np.fromfile('figure_problem_set_2',dtype=d) #input file is big endian 2-byte int
    im = im[64:]   #there seem to be 64*2 extra bytes in this file at the beginning
    im.shape = shape
    
    return im.astype(np.int16)

#####Interpolation Schemes######################################################

#nearest neighbor interpolation
def interp_nearest(im, point):
    i,j = point
    l = np.around(i)
    k = np.around(j)
    
    #only return points that existed in the original image
    if (0<=l<im.shape[0])*(0<=k<im.shape[1]):
        return im[l,k]
    else:
        return 0

#linear interpolation
def interp_lin(im, point):
    i,j = point
    l,k = np.floor(i),np.floor(j)
    a = (i-l)
    b = (j-k)
    
    #only return points that existed in the original image
    if (0<=l<im.shape[0]-1)*(0<=k<im.shape[1]-1):
        return (1-a)*(1-b)*im[l,k] + a*(1-b)*im[l+1,k] + (1-a)*b*im[l,k+1] + a*b*im[l+1,k+1]
    else:
        return 0

ischemes = {'nearest':interp_nearest, 'linear':interp_lin}

#####Linear Transforms##########################################################

#rotate an image by an angle theta (in degrees) counterclockwise
#about center using interp as the interpolation function
def rotate(im, theta, interp='nearest', reshape=False):
    interpolate = ischemes[interp]
    theta *= np.pi/180 #convert to rad from deg
    shape = np.array(im.shape)
    center = shape/2
    
    # if desired set shape of new image so that no info gets lost in the rotation
    if reshape:
        d = eight_dist(shape)   #diameter of rotation
        newshape = np.ceil(np.abs(shape*cos(theta))+np.abs(d*sin(theta)))
    else:
        newshape = shape
    center2 = newshape/2
    im_rot = np.zeros(newshape)
        
    #inverse rotation matrix to map points from new im to old im
    irotmat = np.array([[cos(theta), -sin(theta)],
                        [sin(theta), cos(theta)]])
                        
    for i in range(im_rot.shape[0]):
        for j in range(im_rot.shape[1]):
            #find point in original image that corresponds to point in new image
            #adjust for center of rotation and new size
            point = np.dot(irotmat,np.array([i,j])-center2)+center
            im_rot[i,j] = interpolate(im, point)
    
    return im_rot
  
#####Edge Processing############################################################

#return response of image with 3x3 sobel operators
def edge_sobel(im):
    #define different filters
    h1 = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
    h2 = np.array([[0,1,2],[-1,0,1],[-2,-1,9]])
    h3 = h1[::-1].T
    
    im1 = 1.0*convolve(im,h1)
    im2 = 1.0*convolve(im,h2)
    im3 = 1.0*convolve(im,h3)
    
    return im1,im2,im3

#find edge magnitudes and directions using the sobel operator
#optionally encode direction data into octary
def edges(im, encode=False):
    im1,im2,im3 = edge_sobel(im)
    mags = np.sqrt((im1**2) + (im3**2))

    #get dirs by taking inverse tan
    #convert to degrees, and shift so that
    #discontinuity in theta occurs on positive x-axis
    dirs = atan2(im1,im3) * 180/np.pi + 45
    
    dirs2 = np.zeros(dirs.shape)


    #Create an octary image by separating the angles into directions according to the following matrix
    #  3  2  1
    #  4  X  0
    #  5  6  7
    #(split angles at 45deg increments)
    #effectively shift theta=0 by 22.5 degrees
    #so that all the angles pointing in direction 7 are counted together
    dirsplit = np.arange(-157.5,202.5+1, 45)
    dirs[dirs<-157.5] += 360
    for i in range(8):
        dirs2[(dirsplit[i]<=dirs)*(dirs<dirsplit[i+1])] = i
    
    if encode:
        return mags, dirs2
    else:
        return mags, dirs