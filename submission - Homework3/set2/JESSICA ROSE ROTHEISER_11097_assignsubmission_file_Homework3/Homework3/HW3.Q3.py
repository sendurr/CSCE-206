def minmaxave(numbers):
	#min
	print ("minimum value=", min(numbers))
	#max 
	print ("maximum value=", max(numbers))
	#average
	average= sum(numbers)/float(len(numbers))
	print ("average=","%.3f" %average)

print (minmaxave([3,5,2.3,5,10,4.2]))