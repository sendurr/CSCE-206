'''################################################################################
        CSCE 206 Homework - 1 , Exercise 1.10
                Evaluate a Guassian function
                        
                Author:   Sendurr Selvaraj
                Email:    sendurr@hotmail.com
################################################################################'''

import math

x=1.0
m=0.0
s=2.0

temp = (-0.5)*(((x-m)/s)**2.0)
temp1 = math.sqrt(2.0*math.pi)*s
temp2 = 1.0 / temp1
output = temp2 * math.exp(temp)

print " The Gaussian output  of f(1) is " + str(output)


'''################################################################################
        End of Program
################################################################################'''
