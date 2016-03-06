# Jeremy Abrams
# CSCE 206
# Lab 6 - f2c_qa2.py
# February 11, 2016

import sys

fahrenheit = float(sys.argv[1])
print ("The temperature in Fahrenheit is: ", fahrenheit)
celcius = (fahrenheit-32) * (5/9)
print ("The temperature in Celcius is: ", celcius)