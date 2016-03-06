M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_sum = 0
for i in M:
	for j in i:
		matrix_sum += j
answer = matrix_sum - M[1][1]
print answer
