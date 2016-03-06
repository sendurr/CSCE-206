import statistics
mylist=[3,5,2.3,5,10,4.2]
def minmax(num):
	minimum=num[0]
	maximum=num[0]
	for k in num:
		if k < minimum:
			minimum = k
		if k > maximum:
			maximum = k
	return(minimum,maximum)
def ave(num):
	sumofnum=0
	for n in num:
		sumofnum+=n
		avg=float((sumofnum))/len(num)
	return(avg)
def minmaxave(num):
	return(minmax(num),ave(num))
print(minmaxave(mylist))
