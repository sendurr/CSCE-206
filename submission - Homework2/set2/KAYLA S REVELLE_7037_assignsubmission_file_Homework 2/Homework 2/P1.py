
series = [0,1]

for i in range (1,999):
	series.append(series[i]+series[i-1])

print (series)
print (len(series))
