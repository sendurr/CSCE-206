# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 20:55:05 2016

@author: Tret Burdette
"""

vo=1.0
g=9.81
t=[0.0,.2,.4,.6,.8,1.0,1.2,1.4,1.6,1.8,2.0]
for i in t:
    y=vo*i-(.5*g*i**2)
    print i, y