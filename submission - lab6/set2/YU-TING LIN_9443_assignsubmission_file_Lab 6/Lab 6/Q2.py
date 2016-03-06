import sys
from math import *
print sys.argv

fahrenheit = float(input('Enter degree Fahrenheit: '))
celsius= (fahrenheit - 32)/1.8  
print('%0.1f degree fahrenheit is equal to %0.1f degree celsius' %(fahrenheit, celsius))