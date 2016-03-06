# Jeremy Abrams
# CSCE 206
# Lab 4 - Primes
# February 4, 2016


primes = [2, 3, 5, 7, 11, 13]

counter = 0

print "Before Append: "
for counter in primes:
	print counter

p = 17
primes.append(p)

print "\nAfter Append: "
for counter in primes:
	print counter
