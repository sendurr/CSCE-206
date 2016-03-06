#I set x=0 in order to calculate the polynomial with roots of -1, 1, and 2

x = 15
r0 = -1
r1 = 1
rn = 2
px=1
roots = [r0, r1, rn]

for i in roots:
	px = px*(x-i)

print px

