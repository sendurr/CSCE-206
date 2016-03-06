import math

def area(vertices):
	xy = []
for pair in vertices:
	for i in pair:
		xy.append(i)

x1 = xy [0]
x2 = xy [2]
x3 = xy [4]
y1 = xy [1]
y2 = xy [3]
y3 = xy [5]

area = 0.5*math.fabs((x2*y3)-(x1*y3)+(x3*y1)+(x1*y2)-(x2*y1))
print (area([[0,0][1,0][0,2]]))



