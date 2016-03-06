def min_max_ave(numbers):
	return min(numbers),max(numbers), float(sum(numbers))/len(numbers)

print min_max_ave([3,5,2.3,5,10,4.2])