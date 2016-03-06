# minmaxave(numbers) = [3,5,2.3, 5,10,4.2]
# def minmaxave(numbers):
	# ma=max(nuumbers)
	# mi=min(numbers)
	# av=sum(numbers)/len(numbers)
	# return ma, mi, av

minmaxave= [3,5,2.3,5,10,4]

total=0
for number in minmaxave:
	total+=number
	
average =total/len(minmaxave)
print "average=",average 
maximum=0
minimum=[0]
for c in minmaxave:
	if c > maximum:
		maximum=c
	if c < minimum:
		minimum=c

print("MAX:",maximum)
print("MIN:",minimum)