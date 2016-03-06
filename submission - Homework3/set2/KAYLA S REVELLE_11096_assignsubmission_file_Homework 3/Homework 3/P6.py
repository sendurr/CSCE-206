import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-v', action='store', dest='v',default=0, help='Farenheit Temperature: ')
parser.add_argument('-t', action='store', dest='t',default=0, help='Celsius Temperature: ')
args = parser.parse_args()


g=9.81
try:
	v=float(args.v)
except:
	print("Error: Input must be a number")
	v=eval(input('v = ?\n'))


try:
	t=float(args.t)
except:
	print ("Error: Input must be a number")
	t=eval(input('t=?\n'))


y=v*t-0.5*g*t**2

print (y)