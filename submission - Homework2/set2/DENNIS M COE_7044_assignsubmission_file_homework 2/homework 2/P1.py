l = [0,1]

for i in range(1,999):
	l.append(l[i]+l[i-1])


print l
print len(l)