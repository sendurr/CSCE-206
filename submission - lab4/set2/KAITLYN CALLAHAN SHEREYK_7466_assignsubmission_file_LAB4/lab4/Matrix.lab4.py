M=[[1,2,3],[4,5,6],[7,8,9]]
total=0
for x in M:
	print x, sum(x)
	total+=sum(x)
print "total=%f"%total
