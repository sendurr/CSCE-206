import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-F', action='store', dest='Fahrenheit',default="F", help='degrees fahrenheit')
parser.add_argument('-C', action='store', dest='Celsius',default="C", help='degrees celsius')                            
args = parser.parse_args()

print ("degrees C=", args.Celsius)
print ("degrees F=", args.Fahrenheit)

#def C(F):
#	C=(F-32.0)*(float(5)/9.0)
#	print (C)

if args.Celsius=="C":
	F=float(args.Fahrenheit)
	C=(F-32.0)*(float(5)/9.0)
	print ("C=", "%.2f"%C)
if args.Fahrenheit=="F":
	C=float(args.Celsius)
	F=C*(float(9)/5.0)+32
	print ("F=", "%.2f"%F)


