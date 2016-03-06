
t=input("temperature in degrees Fahrenheit:")
try:
	t=float(t)
	c=5.0/9*(t-32)
	print("temperature in Celsuis=",c)
except:
	print("input temperature must be a number")