'''################################################################################
    CSCE 206 Homework - 3 , Exercise P6
        user input to a formula through argparse and error exceptions
             
        Author:   Sendurr Selvaraj
        Email:    sendurr@hotmail.com
################################################################################'''
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v","--velocity" , help="Enter the value of v0")
parser.add_argument("-t", "--time",  help="Enter the value of t")
args = parser.parse_args()

v0 = args.velocity
t = args.time

g=9.81
while True:
	try:
		y= (float(v0) * float(t) ) - (0.5 * g * (float(t)**2))
		break
	except ValueError:
		print ("Invalid number. Try again using raw input..")
		t = raw_input('Enter the Value of \'t\':')
		v0 = raw_input('Enter the Value of \'v0\':')
	

print ("\n The output is "+ str(y))


 
'''################################################################################
    End of Program
################################################################################'''

