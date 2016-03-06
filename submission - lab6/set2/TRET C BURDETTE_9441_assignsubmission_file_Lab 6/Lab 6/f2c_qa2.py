# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 20:52:57 2016

@author: Tret Burdette
"""

import sys
print sys.argv

def celcius(argv):
    F=float(argv[1])
    C=(F-32.0)*(5.0/9.0)
    print C
