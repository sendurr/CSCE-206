def area(vertices):
	area = 1/2*(vertices[1][0]*vertices[2][1]-vertices[2][0]*vertices[1][1]-vertices[0][0]*vertices[2][1]+vertices[2][0]*vertices[0][1]+vertices[0][0]*vertices[1][1]-vertices[1][0]*vertices[0][1])
	print area

area([[0,0],[1,0],[0,2]])