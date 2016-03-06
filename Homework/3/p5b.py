'''################################################################################
    CSCE 206 Homework - 3 , Exercise P5b
        user input to a formula through argparse
             
        Author:   Sendurr Selvaraj
        Email:    sendurr@hotmail.com
################################################################################'''
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v","--velocity", type=float, help="Enter the value of v0",required=True)
parser.add_argument("-t", "--time", type=float, help="Enter the value of t",required=True)
args = parser.parse_args()

v0 = args.velocity
t = args.time

g=9.81
y= (float(v0) * float(t) ) - (0.5 * g * (float(t)**2))

print ("\n The output is "+ str(y))


 
'''################################################################################
    End of Program
################################################################################'''

