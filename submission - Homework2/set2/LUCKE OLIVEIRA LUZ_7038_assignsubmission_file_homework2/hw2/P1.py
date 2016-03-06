# Name: Lucke Oliveira Luz			Assignment: Homework 2       Exercise: 1

series = [0,1]
i = 0

while len(series) < 1000:
	series.append(series[i]+series[i+1])
	i += 1

print "SERIES =", series	