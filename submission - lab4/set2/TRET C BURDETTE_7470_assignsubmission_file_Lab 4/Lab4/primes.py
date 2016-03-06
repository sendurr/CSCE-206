# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 16:44:04 2016

@author: Tret Burdette
"""

primes=[2,3,5,7,11,13]
for x in primes:
    print "list element:", x
p=[17]
primes.extend(p)
print primes