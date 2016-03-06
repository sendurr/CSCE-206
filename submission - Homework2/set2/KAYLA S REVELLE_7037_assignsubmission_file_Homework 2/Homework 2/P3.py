
h = 0.01
emptylist = []

for i in range(0,101):
	emptylist.append(1+i*h)
for x in emptylist:
	print ("%3.2f" % x)