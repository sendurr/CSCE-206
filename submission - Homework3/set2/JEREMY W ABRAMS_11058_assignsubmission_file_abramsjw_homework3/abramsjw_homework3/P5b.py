# Jeremy Abrams
# CSCE 206
# Homework 3 - P5b.py
# February 18 2016

import argparse

parser = argparse.ArgumentParser(description='Computes Rate of Acceleration')
parser.add_argument('-v', type = float, help = "Used to enter v0 value")
parser.add_argument('-t', type = float, help = "Used to enter t value")

args = parser.parse_args()

v0 = args.v
t = args.t
g = 9.81

y = v0*t - 0.5*g*t**2

print (y)