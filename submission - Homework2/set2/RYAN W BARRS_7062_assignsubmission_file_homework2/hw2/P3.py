coordinates = []
x = 1
h = 0.01

for i in range(0, 101):
	step = i*h
	coordinates.append(x + step)
print coordinates