primes = [2, 3, 5, 7, 11, 13]

for number in primes:
	print number

p = 17
primes.append(p)
print primes


s = 0
M = 150 #M can be any number
k = 1

for i in range(k, M + 1):
	s += float(1)/i
print s

s = 0
M = 150 #M can be any number
j = 1

while j <= M:
	s += float(1)/j
	j += 1
print s


M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = sum(M[0])
l = k + sum(M[2])
d = l + M[1][0] + M[1][2]

print d