# Name: Lucke Oliveira Luz           Assignment: Lab 4      Exercise: 2

M = range(1,11)
s = 0

for k in M:
	s += 1/float(k)

print "SUM_FOR =", s

s = 0
k = 1
M = 10
while k <= M:
	s += 1/float(k)
	k += 1

print "SUM_WHILE =", s