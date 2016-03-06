values=[2,5,7,4,8,3,5]
numbers=[]
for x in values:
	items=x.strip().split(",")
	try:
		numbers.append(float(items))
	except:
		continue
def minmaxave(numbers):
	return "min:",min(numbers)
	return "max:",max(numbers)
	ave=sum(numbers)/(len(numbers)
	return ave
print minmaxave(numbers)