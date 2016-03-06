import sys

if len(sys.argv)>1:
	F=float(sys.argv[1])
else:
	F=float(input('Enter degree Fahrenheit: '))

celcius=(F-32)*5/9

print celcius