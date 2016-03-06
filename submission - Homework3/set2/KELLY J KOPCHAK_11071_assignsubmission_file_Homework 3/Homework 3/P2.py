total=0
n=[2,5,7,4,8,3,5]
def sumoddnumber(n):
	for i in n:
		if i%2==1:
			global total
			total+=i
			i=+1
sumoddnumber(n)
print "sum=", total