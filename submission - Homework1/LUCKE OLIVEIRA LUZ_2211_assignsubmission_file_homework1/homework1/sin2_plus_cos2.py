# Name: Lucke Oliveira Luz   Assignment: Homework 1   Exercise: 1.9

#from math import sin,cos ------> ERROR: IT IS NECESSARY TO IMPORT PI NUMBER ALSO
from math import sin,cos,pi
x = pi/4
#1_val = sin^2(x) + cos^2(x) ------> ERRORS: 1 - VARIABLE NAME CANNOT START WITH A NUMBER / 2 - EXPONENTIATION SIGN ISN'T (^) IN PYTHON
val_1 = (sin(x))**2 + (cos(x))**2
#print 1_VAL  ---------> ERROR: PYTHON DIFFERENTIATE CAPITAL LETTERS FROM LOWER CASE LETTERS IN VARIABLE NAMES
print val_1