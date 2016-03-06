import argparse
# this sets the tone for the fundamentals of the argparse argument that we want to be able to run the temperature conversion program

parser=argparse.ArgumentParser()

parser.add_argument('-f', action='store', dest='f',default=0, help='Temp in Farenheit:')
parser.add_argument('-c', action='store', dest='c',default=0, help='Temp in Celcius:')

args=parser.parse_args()


# Setting tone with definition of the temperature functions and how they will be interpreted from the argparse code



cels=float(args.c)

Faren = (-32+cels)/1.8

faren=float(args.f)

Cels = 32+(9/5*cels)




# if and else statements specify output conditions that make the program run accordingly

if faren != 0:
	print (Faren, "temperature in Celsius")
	print (faren, "INPUT")



else:
	print (Cels, "Temperature in Farenheit")
	print (cels, "INPUT")
	