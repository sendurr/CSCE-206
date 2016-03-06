'''################################################################################
    CSCE 206 Lab - 7 , Exercise P3
        Fahrenheit to Celsius through argparse
             
        Author:   Sendurr Selvaraj
        Email:    sendurr@hotmail.com
################################################################################'''
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f","--Fahrenheit", type=float, help="Enter the temperature in Fahrenheit")
parser.add_argument("-c", "--Celsius", type=float, help="Enter the temperature in Celsius")
args = parser.parse_args()


if args.Fahrenheit:
	f= args.Fahrenheit
	c= (float(f)-32.0)/(1.800)
	print ("\nThe Temperature of "+ str(f) +" Fahrenheit = " + str(c) + "'c")
elif args.Celsius:
	c= args.Celsius
	f= (float(c)*1.800) + 32.00
	print ("\nThe Temperature of "+ str(c) + "'c = " + str(f) +" Fahrenheit")

else:
	print "Incorrect input"


 
'''################################################################################
    End of Program
################################################################################'''

