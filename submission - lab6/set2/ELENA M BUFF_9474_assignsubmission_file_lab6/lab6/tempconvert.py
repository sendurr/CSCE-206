import argparse

parser = argparse.ArgumentParser (description='Convert temperatures.')

parser.add_argument('-f', action='store', dest='f', default=0, type=float, help='temperature in Fahrenheit')
parser.add_argument('-c', action='store', dest='c', default=0, type=float, help='temperature in Celcius')                            
parser.add_argument("-v", "--verbosity", action="count", default=0)
parser.add_argument('--version', action='version', version='%(prog)s 1.0')
args = parser.parse_args()

# print (args.f)
# print (args.c)

# x=eval(args.f)
# y=eval(args.c)

Celcius=(args.f-32)*(5./9)
Fahrenheit=(9./5)*args.c+32


# print (Celcius)

# print (Fahrenheit)

if __name__ == '__main__':	
	if not args.f==0:
		print ("input: ",args.f,'degree(F)')
		print ("output: ","%.2f"%Celcius, 'degree(C)')
	if not args.c==0:
		print ("input: ",args.c,'degree(C)')
		print ("output: ","%.2f"%Fahrenheit, 'degree(F)')



