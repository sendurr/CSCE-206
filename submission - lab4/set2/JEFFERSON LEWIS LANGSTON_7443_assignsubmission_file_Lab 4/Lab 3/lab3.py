#Problem 1
L1 = [2, 3, 5, 7, 11, 13]
for x in L1:
	print x
f = 17
L1.append(f)
print L1

#Problem 2
f = 0
g = 3
h = 1
for n in range(h,g+1):
	f = f + (1.00/n)
print f

#Problem 3
Matrix = [[1,2,3],[4,5,6],[7,8,9]]
print Matrix
sum = 0
for n in range(len(Matrix)):
	for s in range(len(Matrix[n])):
		if n == 0 or n == 2 or s == 0 or s == 2:
			sum+=Matrix[n][s]
			print sum

