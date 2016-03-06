import argparse

try:
	parser = argparse.ArgumentParser()
	parser.add_argument("--v", "--initial_velocity", type=float)
	parser.add_argument("--t", "--time", type=float)
	args = parser.parse_args()
	v = args.v; t = args.t; g=9.81
	y =v*t-0.5*g*t**2
	print(y)
except ValueError:
	print("Error: Input actual integers")
if False:
	T=input("what is T?")
	print("t="+t)
	V=input("what is V?")
	print("V="+V)
	g=9.81
	y=int(float(V))*int(float(T))-0.5*g*int(float(T))**2
	print(y)