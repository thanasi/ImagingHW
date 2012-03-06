from ball import *


im = rl2im(None,fn='out2.txt')
im2,samples = resample(im,newshape=(8,8))

qt = im2qt(im2)

imsave('1-3a.png',im)
imsave('1-3b.png',(im-im*samples,im-im*samples,im*(1-samples)+samples))
imsave('1-3c.png',im2)

with open('out3.txt','w') as outfile:
    outfile.write(qt)
