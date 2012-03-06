#!/usr/local/bin/ipython
# Athanasios Athanassiadis March 2012

import os
from pylab import *
from scipy.misc import imsave, imread
import numpy as np
from numpy.linalg import eig

cov = np.cov

folder = 'faces'

ion()


##############################################################################

C = cov(testfaces.T)

eigvals, eigvects = eig(C)

eigfaces_unsorted = np.dot(testfaces, eigvects).T

eigenzip = zip(eigvals, eigfaces_unsorted)
eigenzip.sort(key=lambda x: x[0])

eigfaces = np.array([pair[1] for pair in eigenzip[::-1]], dtype=np.int16)

##############################################################################

checkface = origfaces[0]

weights = []

n=8

for i in range(n):
    weights.append( (eigfaces[i] * (checkface).flatten()).sum() )

# normalize weights
weights = np.array(weights, dtype=np.float)
weights /= np.sqrt((weights**2).sum())

approxes = np.zeros((n, checkface.flatten().shape[0]))

for i in range(n):
    approxes[i] = (approxes.sum(0) + weights[i] * eigfaces[i])

