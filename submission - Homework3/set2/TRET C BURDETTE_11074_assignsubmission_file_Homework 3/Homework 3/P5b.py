# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 17:30:28 2016

@author: Tret Burdette
"""

import sys
import argparse

def trajectory(v0, t):
    v0 = float(v0)
    t = float(t)
    g = 9.81
    y = v0*t-.5*g*t**2
    return y

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--velocity', default=5)
    parser.add_argument('-t', '--time', default=.8)
    args = parser.parse_args()
    print trajectory(args.velocity, args.time)


if __name__ == '__main__':
    main()