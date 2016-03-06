def area (vertices):
	x1=vertices[0][0]
	y1=vertices[0][1]
	x2=vertices[1][0]
	y2=vertices[1][1]
	x3=vertices[2][0]
	y3=vertices[2][1]
	A=0.5*((x2*y3)-(x3*y2)-(x1*y3)+(x3*y1)+(x1*y2)-(x2*y1))
	print A

area([[0,0],[1,0],[0,2]])