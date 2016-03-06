# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 16:54:54 2016

@author: Tret Burdette
"""

from math import*

def area(x1,y1,x2,y2,x3,y3):
    A=0.5*abs(x2*y3 - x3*y2 - x1*y3 + x3*y1 + x1*y2 - x2*y1)
    return A
print "area=", area (0,0,1,0,0,2)
