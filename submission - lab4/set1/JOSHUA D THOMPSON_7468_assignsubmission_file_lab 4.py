# Josh Thompson Lab 4 Assignment

primes = [2,3,5,7,11,13]

for number in primes:
	print "Each Prime:", number

p = 17

primes.append(p)

print primes


#############################################
# While Loop Solution

s = 0
M = 100
k = 1
while (s < 100):
	print "total is:", s
	s += 1/k
	

print "Done"

# For Loop Solution
# Cannot solve entire problem, this is the best code that I could come up with
# s = 0  
# k = 1
# M = 100
# for k in s:
#     s += 1/k
#     print s

m= [[1,2,3],[4,5,6],[7,8,9]]

total=0 
for x in m:
	# m.pop(5) This is the only thing I couldn't get to work to remove the middle variable and sum the matrix
	print x, sum(x)
	total += sum(x)
print "total=%f"%total

