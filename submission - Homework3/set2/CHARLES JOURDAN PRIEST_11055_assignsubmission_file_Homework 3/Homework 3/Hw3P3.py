def minmaxave(numbers):
	min_=min(numbers)
	max_=max(numbers)
	avg=sum(numbers)/float(len(numbers))
	return min_, max_, avg

print (minmaxave([3,5,2.3,5,10,4.2]))