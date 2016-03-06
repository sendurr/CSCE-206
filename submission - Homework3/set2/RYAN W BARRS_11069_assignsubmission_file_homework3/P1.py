def area(vertices):
	x1y1 = vertices[0]
	x2y2 = vertices[1]
	x3y3 = vertices[2]

	A = 0.5 * abs(x2y2[0]*x3y3[1] - x3y3[0]*x2y2[1] - x1y1[0]*x3y3[1] + x3y3[0]*x1y1[1] + x1y1[0]*x2y2[1] - x2y2[0]*x1y1[1])
	return A

triangle = [[0,0], [1,0], [0,2]]
print "area =", area(triangle)