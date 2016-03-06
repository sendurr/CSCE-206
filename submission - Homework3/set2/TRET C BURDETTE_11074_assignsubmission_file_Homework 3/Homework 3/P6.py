# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 17:49:13 2016

@author: Tret Burdette
"""

import sys
print sys.argv

v0=float(raw_input("please enter a velocity:"))
t=float(raw_input("please enter a time:"))
g=9.81

try:
    v0=float(sys.argv[0])
    t=float(sys.argv[1])
except:
    print "You failed to provied a correct velocity (number only)"
    print "You fialed to provide a correct time (number only)"
y=v0*t-.5*g*t**2
v0=float(raw_input("please enter a correct velocity:"))
t=float(raw_input("please enter a correct time:"))
y=v0*t-.5*g*t**2
print y