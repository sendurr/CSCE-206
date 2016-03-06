#Begin Question 1
print "Question 1."

primes = {2, 3, 5, 7, 11, 13}
#makes list
for x in primes:
	print x
#prints each list item separately
p = 17

primes = list(primes)
#converts list to list
primes.append(p)
#adds p
print primes
#prints list as a list
print " "
#End Question 1

#Begin Question 2
print "Question 2."
M = 20
total1a = 0.0
k = 0.0

for k in range(1,M):
	total1a = total1a + 1/k
#this loop doesn't work, can't figure out why	
print total1a

M = 20
total1b = 0.0
k = 1.0

while k < M:
	total1b = total1b + 1/k
	k = k + 1
#I think this works?
print total1b
print ""
#End Question 2

#Begin Question 3
print "Question 3."

M = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

total3 = M[0][0]+M[0][1]+M[0][2]+M[1][0]+M[1][2]+M[2][0]+M[2][1]+M[2][2]
#manually calls and sums all pieces of matrix except [1][1], or the center
print total3
#End Question 3