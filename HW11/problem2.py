#!/usr/local/bin/ipython
# Athanasios Athanassiadis March 2012
from eigenface import *

infolder = 'faces'
outfolder = 'eigenfaces'
outfolder2 = 'face_approx'

print 'loading faces'
facearr, shape = load_faces(infolder)
print 'computing eigenfaces'
eigfaces = eigenfaces(facearr, 8)
print 'saving output'
for i in range(len(eigfaces)):
    imsave(os.path.join(outfolder,'eigenface%d.png' % i), 
           eigfaces[i].reshape(shape))
    
print 'calculating approximation faces for first face'
face = facearr[:,0]

fapproxes = approxiface(face, eigfaces, 5)

print 'saving output'
imsave(os.path.join(outfolder2, 'original.png'),
       face.reshape(shape))

for i in range(len(fapproxes)):
    imsave(os.path.join(outfolder2, 'approx%d.png' % (i+1)),
           fapproxes[i].reshape(shape))

