'''################################################################################
    CSCE 206 Homework4  , Exercise Q4
    sincos(x) function
    
    Author:   Sendurr Selvaraj
    Email:    sendurr@hotmail.com
################################################################################'''

import numpy as np
from math import *

def sincos(x):
	return np.sin(np.cos(x))

x=[1,3,5,7,10.5]

print ("For the array " + str (x))
print ("sin(cos(x)) = " + str (sincos(x)))

'''################################################################################
    End of Program
################################################################################'''
