'''################################################################################
    CSCE 206 Homework5  , Exercise Q2
    Geometric Shapes
    
    Author:   Sendurr Selvaraj
    Email:    sendurr@hotmail.com
################################################################################'''

from math import * 

class rectangle:
	def __init__(self, x0, y0):
		self.x0=x0
		self.y0=y0

	def area(self):
		x0 , y0 = self.x0 , self.y0
		area_result = x0 * y0
		print ("The area of a rectangle with width = " + str(x0) + " height = " + str(y0) + " is " + str(area_result))

	def circumference(self):
		x0 , y0 = self.x0 , self.y0
		circum_result = 2*(x0 + y0)
		print ("The circumference of a rectangle with width = " + str(x0) + " height = " + str(y0) + " is " + str(circum_result))

class triangle:
	def __init__(self, x0, y0 , x1 , y1 , x2 , y2):
		self.x0=x0
		self.y0=y0
		self.x1=x1
		self.y1=y1
		self.x2=x2
		self.y2=y2

	def area(self):
		x0 , y0 , x1 , y1 , x2 , y2= self.x0 , self.y0 , self.x1 , self.y1 , self.x2 , self.y2
		area_result = ((x0*y1) + (x1*y2) + (x2*y0) - (y0*x1) - (y1*x2) - (y2*x0)) / 2.0
		area_result = abs(area_result)
		print ("The area of a triangle with coordinates A(%.2f,%.2f) , B(%.2f,%.2f) , C(%.2f,%.2f) is %.2f " %(x0,y0,x1,y1,x2,y2,area_result))

	def circumference(self):
		x0 , y0 = self.x0 , self.y0
		x0 , y0 , x1 , y1 , x2 , y2= self.x0 , self.y0 , self.x1 , self.y1 , self.x2 , self.y2
		a = sqrt((x0 - x1)**2 + (y0 - y1)**2)
		b = sqrt((x1 - x2)**2 + (y1 - y2)**2)
		c = sqrt((x2 - x0)**2 + (y2 - y0)**2)
		circum_result = (a + b + c)
		print ("The circumference of a triangle with coordinates A(%.2f,%.2f) , B(%.2f,%.2f) , C(%.2f,%.2f) is %.2f " %(x0,y0,x1,y1,x2,y2,circum_result))

r1 = rectangle(4.9, 2.5)
r1.area()
r1.circumference()
t1 = triangle(-2.0 , 3.0 , -3.0 , -1.0 , 3.0 , -2.0)
t1.area()
t1.circumference()




'''################################################################################
    End of Program
################################################################################'''
