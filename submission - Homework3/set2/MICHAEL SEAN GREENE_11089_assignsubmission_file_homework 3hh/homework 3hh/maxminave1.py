def minmaxave(alist):
    max, average, min = alist[0]
    for i in alist[1:]:
        if i[0] >max: max = i[0]
        average += i[1]
        if i[2] < min: min = i[2]
    	average = average / len(alist)
    	return max, average, min
print minmaxave([3,5,2,3,5,10,4,2])