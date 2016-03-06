M=13
sumation=0.0
for k in range(1,M+1):
	sumation=sumation+(1.0/float(k))
	print sumation
print "^^for loop^^"
while k<M:
	sumation=sumation+(1.0/float(k))
	k+=1
print sumation
print "^^while loop^^"
print "#############"
print "?3 on lab4"
Matrix=[[1,2,3],[4,5,6],[7,8,9]]
print Matrix[0]
print Matrix[1]
print Matrix[2]
del Matrix[1][1]
total=0
for x in Matrix:
	print x, sum(x)
	total+=sum(x)
print "total=%f"%total