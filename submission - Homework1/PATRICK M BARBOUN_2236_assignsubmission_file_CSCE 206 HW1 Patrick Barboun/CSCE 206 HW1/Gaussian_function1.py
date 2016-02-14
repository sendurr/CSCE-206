from math import pi, exp 
import matplotlib.pyplot as plt
#Need to import math functions pi and exp
m = 0
s = 2
x = 1
#Defined the necessary variables
f = 1/(((2*pi)**0.5)*s)*exp(-0.5*((x-m)/s)**2) 
print f
#Define the gaussian function and print the answer