series = [0, 1]
i = 0
while i <= 999:
	if i >= 2:
		series.append(series[i-1] + series[i-2])
	i += 1
print series