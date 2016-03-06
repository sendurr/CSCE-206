
import sys
print (sys.argv)


t=input("temperature in degrees Fahrenheit:")
try:
	t=float(t)
except:
	print ("Error:Input value is NOT a number")
	sys.exit(-1)


c=5.0/9*(t-32)
print (c)	