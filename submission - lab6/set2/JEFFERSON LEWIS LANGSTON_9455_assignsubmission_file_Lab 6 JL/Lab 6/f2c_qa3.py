import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-f','--f', type = float)
parser.add_argument('-c','--c', type = float)
args = parser.parse_args()
f = args.f
c = args.c

if f! = none:
	Celcius = ((f-32)*(5.0/9))
	print 'Input = %f degree(F)'%Fahrenheit
	print 'Output = %f degree(C)'%Celcius

if c! = none:
	Fahrenheit = (c*(9.0/5))+32
	print 'Input = %f degree(C)'%Celcius
	print 'Output = %f degree (F)'%Fahrenheit




