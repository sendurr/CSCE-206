#Q2
def sumoddnumber(integers):
	s=0
	for x in integers:
		if x%2 != 0:
			s+= x
	print "sum=",s
integers=[2,5,7,4,8,3,5]
sumoddnumber(integers)