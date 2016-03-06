def area(vertices):
	v = vertices
	a = 0.5*(v[1][0]*v[2][1]-v[2][0]*v[1][1]-v[0][0]*v[2][1]+v[2][0]*v[0][1]+v[0][0]*v[1][1]-v[1][0]*v[0][1])
	return a

print area([[0,0],[1,0],[0,2]])