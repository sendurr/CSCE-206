import argparse
try:
	parser = argparse.ArgumentParser()
	parser.add_argument('-v', action='store', dest='v')
	parser.add_argument('-t', action='store', dest='t')                            
	args = parser.parse_args()
	v0=float(v)
	t=float(t)
	y=v0*t-0.5*g*t**2
	print (y)
except:
	print ("Error.")
	v0=float(input("Enter v0"))
	t=float(input("Enter t"))
	y=v0*t-0.5*g*t**2
	print (y)
