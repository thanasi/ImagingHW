#Athanasios Athanassiadis Jan 2012
from segmentation import *

fig1 = np.fromfile('figure2_problem_set_3',dtype='>i2').reshape((56,56))
fig1 /= 1.0*fig1.max()

labels,equiv = label_components(fig1)
#number of components is number of entries in the equivalence table equal to themselves
#less one because the background (0) is in there
ncomp = len([i for i in equiv if equiv[i]==i])-1

imsave('3-4a.png',fig1)
imsave('3-4b.png',(labels % 3, labels % 4, labels % 5))

equiv_s = repr(equiv)
with open('problem4.txt','w') as outfile:
    outfile.write('Number of regions: {}\n'.format(ncomp))
    outfile.write('Equivalence Table:\n')
    outfile.write(equiv_s)
