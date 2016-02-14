#import numpy as np
import matplotlib.pyplot as plt
# import sys
from math import *

x= 2.33 #real number
y= -2 #integer
z= "32233"
saying = 'I am a boy'
print(x,y,z,saying)

array1= [3,4.0,34,-5,23]
array1Index= 0

for i in array1:
		if array1Index % 2 == 0:
			print(i)
		array1Index += 1

L= ["good","very good","excellent"]
print(L[0::2])

m= [[0 for x in range(3)] for x in range (3)]
print(m)
m= [[1,2,3],[4,5,6],[7,8,9]]
print(m)
print(m[1][1])