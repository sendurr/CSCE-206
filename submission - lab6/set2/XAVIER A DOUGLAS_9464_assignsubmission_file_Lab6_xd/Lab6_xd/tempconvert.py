import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-x', action='store', dest='x',default=0, help='Temp Value')
parser.add_argument('-o', action='store', dest='op',default="+", help='Celsius or Fahrenheit')
args = parser.parse_args()

x=eval(args.x)

op=args.op

print (x,op,'=')

if op == "c":
	print ("Convert to Fahrenheit: ", 9.0/5*(x+32))
elif op == "f":
	print ("Convert to Celsius: ", 5.0/9*(x-32))
else:
	print ("ERROR: NON-SPECIFIED TEMPERATURE UNITS")
