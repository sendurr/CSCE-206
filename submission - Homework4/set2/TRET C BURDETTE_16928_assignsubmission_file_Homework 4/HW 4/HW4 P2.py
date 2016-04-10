# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 21:06:27 2016

@author: Tret Burdette
"""

import numpy as numpy
import matplotlib.pyplot as plt
import sys
from pylab import *

x=arange(-3.14,3.14,0.01)
y=(exp(x**2))*sin(x)
plot(x,y)
grid(True)
title('Plot of Figure')
show()