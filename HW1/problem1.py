from ball import *

ball1 = make_ball(10, dmetric='4')
ball2 = make_ball(14, shell=1, center=(4,30))
ball3 = make_ball(8, r2=10, center=(20,11), dmetric='8')
imsave('1-1a.png',ball1)
imsave('1-1b.png',ball2)
imsave('1-1c.png',ball3)
