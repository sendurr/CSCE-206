r1 = -1
r2 = 1
r3 = 2
x = 3
roots = [r1, r2, r3]

product = 1
for i in roots:
	product *= (x - i)
print product