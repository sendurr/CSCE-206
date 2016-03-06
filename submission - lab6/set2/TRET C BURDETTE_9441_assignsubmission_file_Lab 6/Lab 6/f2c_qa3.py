# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 21:06:47 2016

@author: Tret Burdette
"""

import sys
print sys.argv
import argparse

parse=argparse.ArgumentParser()
parse.add_argument('-f', action='store', dest='X')
parse.add_argument('-c', action='store', dest='Y')
args=parse.parse_args()

C=float(((args.X)-32.0)*(5.0/9.0))
print "C=", C

F=float((args.Y)*(9.0/5.0)+32.0)
print "F=", F

#I am unsure how to get command line to work on my PC
#I tried coming by on Friday to ask about it
#It is a desktop PC to I can't bring it to class
#Because of this some of my answers on this and HW3 may be wrong