from ball import *

ball1 = make_ball(10, dmetric='euclid', ret='img')
ball2 = make_ball(10, dmetric='4', ret='img')
ball3 = make_ball(10, dmetric='8', ret='img')
ball4 = make_ball(10, shell=11) 

imsave('1-2a.png',ball1)
imsave('1-2b.png',ball2)
imsave('1-2c.png',ball3)
imsave('1-2d.png',ball4)

with open('out2.txt','w') as outfile:
    outfile.write(im2rl(ball4))
