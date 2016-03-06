def area(vertices):
	point1=vertices[0]
	point2=vertices[1]
	point3=vertices[2]

	a=.5*(point2[0]*point3[1]-point3[0]*point2[1]-point1[0]*point3[1]+point3[0]
		*point1[1]+point1[0]*point2[1]-point2[0]*point1[1])
	return a

triangle = [[0,0],[1,0],[0,2]]

print (area(triangle))