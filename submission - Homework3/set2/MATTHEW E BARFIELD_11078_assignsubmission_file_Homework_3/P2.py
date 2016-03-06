print "Homework 3 - Question 2"
print ""

def sumoddnumber(integers):
	summ=0
	for x in integers:
		if x%2 !=0:
			summ+=x
	print "Sum = ", summ
integers = [2,5,7,4,8,3,5]
sumoddnumber(integers)

