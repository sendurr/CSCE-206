t=raw_input("temperature in F: ")
try:
	t=float(t)
	c=(5.0/9)*t-32
	print "temperature in C.degrees=",c
except:
	print "please input temperture value as number"