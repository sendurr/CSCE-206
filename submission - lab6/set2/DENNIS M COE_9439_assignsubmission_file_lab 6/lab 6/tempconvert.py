import argparse

parser=argparse.ArgumentParser()
parser.add_argument('-f', action='store', dest='f',default=0, help='Temp in Farenheit:')
parser.add_argument('-c', action='store', dest='c',default=0, help='Temp in Celcius:')

args=parser.parse_args()

f=float(args.f)
c=float(args.c)
F = (f-32)/1.8
C = (c*9/5) + 32



if f != 0:
	print (f, "input")
	print (F, "degrees C")

else:
	print (c, "input")
	print (C, "degrees F")
	