# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 17:28:11 2016

@author: Tret Burdette
"""

x={1,3,8,10,14,10,20,25}
print x

y={3,3,8,10,15,20,33,55,88}
print y

print "intersection:", x&y
print "union", x|y
print "in x and not in y", x-y
print "in y and not in x", y-x