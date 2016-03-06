from math import *
print 'Computing a Mathematical Sum'
print ('')

s=0; k=1; m=50
for i in range (k,m+1):
	s+=1.0/i
print 'For Loop Sum'
print 'Sum:', s
print ('')

s=0; k=1.0; m=50
while k <= m:
	s += 1/k
	k += 1
print 'While Loop Sum'
print 'Sum:', s
