def triangle_area(vertices):
	if len(vertices)==3 and len(vertices[0])==2 and len(vertices[1])==2 and len(vertices[2])==2:
		area = (1./2.)*(vertices[1][0]*vertices[2][1]-vertices[2][0]*vertices[1][1]-vertices[0][0]*vertices[2][1]+vertices[2][0]*vertices[0][1]+vertices[0][0]*vertices[1][1]-vertices[1][0]*vertices[0][1])
		return area
	else:
		return 'Error: wrong format'
	
print triangle_area([[0,0],[1,0],[0,2]])
