import sys

for arg in sys.argv:
	tempF = arg
	tempF = float(tempF)
	tempC = (tempF-32)/1.8

print tempC