from math import * #Unnecessary

def vertices(x1,x2,x3,y1,y2,y3):
	A = 0.5*(x2*y3-x3*y2-x1*y3+x3*y1+x1*y2-x2*y1)
	return A
print vertices(0,1,0,0,0,2)



# triangle1 = area(vertices)
# print "Area of triangle is %.2f" % triangle1
