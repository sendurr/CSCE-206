'''################################################################################
    CSCE 206 Homework - 3 , Exercise P5a
        user input to a formula through command line
             
        Author:   Sendurr Selvaraj
        Email:    sendurr@hotmail.com
################################################################################'''

import sys

v0 = sys.argv[1]
t = sys.argv[2]

g=9.81
y= (float(v0) * float(t) ) - (0.5 * g * (float(t)**2))

print ("\n The output is "+ str(y))


 
'''################################################################################
    End of Program
################################################################################'''

