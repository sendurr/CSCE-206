s = [0,1]
n = 2

while n < 17:
	s.append(s[n-2] + s[n-1])
	n+=1

print s
