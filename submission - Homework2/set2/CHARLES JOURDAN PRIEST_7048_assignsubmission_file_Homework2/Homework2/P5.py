root_list = [-1, 1, 2]
p_x = 1
x = 15

for r in root_list:
	p_x *= (x - r)
	print (p_x)
# this just gives each step in the polynomial calculation
print (p_x)
# final result is 72 after each iteration of the for loop
