# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 21:13:46 2016

@author: Tret Burdette
"""

import sys
from numpy import *
from matplotlib.pyplot import *
if len(sys.argv) ==1:
    print 'Enter initial velocity'
    sys.exit(1)

v0_list = [float(v0) for v0 in sys.argv[1:]]
g = 9.81
legends = [] 
for v0 in v0_list:
    v0 = float(v0)
    t_max = 2*v0/g
    t = linspace(0,t_max,100)
    y = v0*t -0.5*g*t**2
    hold(True)
    plot(t,y)
    legends.append('v0=%g'%v0)

show()