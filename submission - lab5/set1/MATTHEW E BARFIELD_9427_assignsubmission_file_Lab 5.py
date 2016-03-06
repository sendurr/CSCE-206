
print "Question 1"
print ("")
def PrintStar(n):
	for i in [n]:
		print ('*'*(i))

PrintStar(1)
PrintStar(10)
PrintStar(100)
print ("")

print "Question 2"
print ("")
def PrintStarX(n, row=0):
	for i in [n]:
		print ('*'*(i))
		print ("")
	for x in range(row):
		print ('*'*(i))

PrintStarX (10,3)



