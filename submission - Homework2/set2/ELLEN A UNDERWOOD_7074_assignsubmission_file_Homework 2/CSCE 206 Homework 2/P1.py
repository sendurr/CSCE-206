a=[]
total=0
for x in range(0,999):
	if x==0:
		b=0
		c=1
		a.append(b)
		a.append(c)
	else:
		d=a[len(a)-2]
		e=a[len(a)-1]
		total=d+e
		a.append(total)
print a
	