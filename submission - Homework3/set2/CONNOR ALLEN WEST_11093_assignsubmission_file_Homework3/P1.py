def area(vertices):
	v1 = (vertices[0][0],vertices[0][1])
	v2 = (vertices[1][0],vertices[1][1])
	v3 = (vertices[2][0],vertices[2][1])
	x1 = (v1[0])
	x2 = (v2[0])
	x3 = (v3[0])
	y1 = (v1[1])
	y2 = (v2[1])
	y3 = (v3[1])
	A = (0.5)*abs(((x2*y3)-(x3*y2)-(x1*y3)+(x3*y1)+(x1*y2)-(x2*y1)))
	print('Area of Triangle is %.2f'%A)
 
area([[0,0], [1,0], [0,2]])