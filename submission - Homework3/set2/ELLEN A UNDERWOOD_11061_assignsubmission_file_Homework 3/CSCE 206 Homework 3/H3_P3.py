maximum=0
minimum=0
ave=0
total=0
def minmaxave(numbers):
	#for x in numbers:
	#	if x[0]>x[1]:
	maximum=max(numbers)
	print ("max=",maximum)
	minimum=min(numbers)
	print ("min=", minimum)
	total=sum(numbers)
	ave=total/len(numbers)
	print ("ave=",float(ave))
minmaxave([3,5,2.3,5,10,4.2])	
