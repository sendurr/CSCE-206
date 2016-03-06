m = [[1,2,3], [4,5,6],[7,8,9]]

total = 0
for i in range(3):
	for j in range(3):
		if m[i][j] == m[1][1]:
			total += 0
		else:
			total += m[i][j]
print "Boundary sum =", total