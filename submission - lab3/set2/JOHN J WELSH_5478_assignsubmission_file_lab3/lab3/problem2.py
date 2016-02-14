#Lab 3 Problem 2 by John Welsh

# 2. while loop application

# starting with 13, add all the odd numbers from 13 up to 999
# save it to variable sum

i = 13
_sum = 0
while i <= 999:
	_sum += i
	i += 2
print _sum