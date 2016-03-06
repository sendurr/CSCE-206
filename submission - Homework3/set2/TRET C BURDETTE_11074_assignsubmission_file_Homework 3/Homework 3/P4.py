# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 17:28:36 2016

@author: Tret Burdette
"""

t=float(raw_input("enter the value for time (number only)"))
v0=float(raw_input("enter the value for velocity (number only)"))
g=9.81
y=v0*t-0.5*g*t**2

print "y=", y