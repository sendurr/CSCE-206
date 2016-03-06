s=[]
def maxminave(numbers):
	s.append(max(numbers))
	s.append(min(numbers))
	ave= sum(numbers)/len(numbers)
	s.append(ave)
	return s
print maxminave([3,5,2.3,5,10,4.2])