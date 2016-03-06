degF=float(input("Enter the degrees F:"))
degC=(degF-32)*(5/9.0)
print ("Degrees in celsius:",degC)



import sys
print ("Enter degrees F:")
degF=float(sys.argv[0])
degC=(degF-32)*(5/9.0)
print ("Degrees in Celsius:",degC)


import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', action='store', dest='degF')
parser.add_argument('-c', action='store', dest='degC')                            
args = parser.parse_args()

if args.degC:
	c=float(degC)
	f=c*1.8+32
	print ("Degrees in F:",args.f)
if args.degF:	
	f=float(degF)
	c=(f-32)*(5/9.0)
	print ("Degrees in C:",args.c)
