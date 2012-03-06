#!/usr/local/bin/ipython
# Athanasios Athanassiadis March 2012
from eigenface import *

infolder = 'faces'
outfolder = 'eigenfaces'
outfolder2 = 'face_approx'

print 'loading faces'
origfaces, faces, shape = load_faces(infolder)
avgface = origfaces.sum(0) / origfaces.shape[0]

print 'computing eigenfaces'
eigfaces = eigenfaces(faces, 8)

print 'saving output'
imsave(os.path.join(outfolder, 'avgface.png'),
       avgface)
       
for i in range(len(eigfaces)):
    imsave(os.path.join(outfolder,'eigenface%d.png' % i), 
           eigfaces[i].reshape(shape))

    
print 'calculating approximation faces for first face'
face = origfaces[0]

fapproxes = approxiface(face.flatten(), eigfaces, avgface.flatten(), 8)

print 'saving output'
imsave(os.path.join(outfolder2, 'original.png'),
       face)

for i in range(len(fapproxes)):
    imsave(os.path.join(outfolder2, 'approx%d.png' % (i+1)),
           fapproxes[i].reshape(shape))

