print "all amounts should be in euros"

while True:
	A=float(raw_input("1000.0"))
	p=float(raw_input("0.05"))
	n=float(raw_input("3.0"))
	I=A * (1 + p/100.0) ** n
	print "Interest is", I,"euros"