#Rachel Smoak
#Homework 3
#28 February 2016

#Question 1

def area(vertices):
	x1=float(vertices[0][0]) #defining these makes it easier for me to use them later
	x2=float(vertices[1][0])
	x3=float(vertices[2][0])
	y1=float(vertices[0][1])
	y2=float(vertices[1][1])
	y3=float(vertices[2][1])
	area = 0.5*abs(x2*y3-x3*y2-x1*y3+x3*y1+x1*y2-x2*y1) #area formula given in question
	print "The area of the triangle is", "%.2f" %area, "units."

area([[0,0],[1,0],[0,2]])