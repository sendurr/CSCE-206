# Jeremy Abrams
# CSCE 206
# Homework 3 - P1.py
# February 18 2016

def area(vertices):
	x1 = vertices[0][0]
	x2 = vertices[1][0]
	x3 = vertices[2][0]
	y1 = vertices[0][1]
	y2 = vertices[1][1]
	y3 = vertices[2][1]
	
	area = (0.5)*((x2*y3) - (x3*y2) - (x1*y3) + (x3*y1) + (x1*y2) - (x2*y1))

	return area

print area([[0,0],[1,0],[0,2]])