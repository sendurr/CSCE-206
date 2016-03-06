series=[0,1]
i=0
value=0
while i<1000:
	value=series[-1]+series[-2]
	series.append(value)
	i+=1
print series
#not sure why "L" shows at the end of many of the printed values