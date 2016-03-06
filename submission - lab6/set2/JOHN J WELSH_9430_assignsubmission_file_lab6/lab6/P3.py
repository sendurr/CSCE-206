import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', action='store', dest='F', type=float, help='Temp. Fahrenheit')
parser.add_argument('-c', action='store', dest='C', type=float, help='Temp. Celsius')                            

args = parser.parse_args()

if args.F:
	print (args.F-32)*5/9
elif args.C:
	print (args.C*9/5)+32
