series = [0,1]
n = 2

while n < 1000:
	series.append(series[n-2] + series[n-1])
	n+=1

print series