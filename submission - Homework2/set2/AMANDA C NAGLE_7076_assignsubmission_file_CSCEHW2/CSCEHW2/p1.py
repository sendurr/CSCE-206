n=[]
total=0
for x in range(0,999):
	if x== 0:
		c=0
		d=1
		n.append(c)
		n.append(d)
	else:
		a= n[len(n)-2]
		b= n[len(n)-1]
		total=a+b
		n.append(total)
print n

