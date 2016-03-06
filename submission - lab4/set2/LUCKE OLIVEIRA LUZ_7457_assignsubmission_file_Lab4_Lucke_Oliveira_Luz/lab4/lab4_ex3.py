# Name: Lucke Oliveira Luz           Assignment: Lab 4      Exercise: 3

M = [[1,2,3],[4,5,6],[7,8,9]]

SUM_BOUND = 0
for i in M:
	for j in i:
		SUM_BOUND += j
SUM_BOUND -= M[1][1]

print "SUM BOUNDARIES =", SUM_BOUND