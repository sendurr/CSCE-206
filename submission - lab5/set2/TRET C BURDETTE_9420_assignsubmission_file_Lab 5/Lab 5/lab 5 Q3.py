# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 22:32:19 2016

@author: Tret Burdette
"""

def checkprime(n):
    for i in range(2,n-1):
        if n%i==0:
            print "false"
        elif n%i>0:
            print "true"
#getting 1 false makes whole test false, ie. not prime