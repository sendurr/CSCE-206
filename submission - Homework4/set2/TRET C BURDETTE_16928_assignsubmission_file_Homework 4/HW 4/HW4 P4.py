# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 21:17:19 2016

@author: Tret Burdette
"""

import numpy as np
from math import *
import sys
x=[1,3,5,7,10.5]
print x
x1=np.array(x)
print x1
def mysincos(x1):
	return np.sin(x)*np.cos(x)
y=mysincos(x1)
print y