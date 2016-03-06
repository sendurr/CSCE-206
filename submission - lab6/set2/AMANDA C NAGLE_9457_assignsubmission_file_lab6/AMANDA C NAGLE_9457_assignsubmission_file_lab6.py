t= raw_input("tempurature in Fahrenheit:")
t= float(t)
C= (t-32)/(1.8)
print "Tempurture in Celcius=", C 

import sys
print "degrees Fahrenheit=", sys.argv[1]
f= float(sys.argv[1])
d= (f-32)/(1.8)
print "degrees Celcius=", d
 
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-f', action= 'store', type= int)
parser.add_argument('-c', action= 'store', type= int)

args = parser.parse_args()

if args.f:
	j= float(args.f)
	i=(j-32)/(1.8)
	print "input: %.2f degree(F)" %args.f 
	print "output: %.2f degree(C)" %i 
else:
	k= float(args.c)
	print "input: %.2f degree(F)" %args.c
	print "output: %.2f degree(F)" %(args.c*1.8+32)
 
