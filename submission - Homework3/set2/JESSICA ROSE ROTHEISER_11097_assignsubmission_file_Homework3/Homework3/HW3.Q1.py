import math
def TriangleArea(X1,Y1,X2,Y2,X3,Y3):
	A = (1/2)*abs(X2*Y3 - X3*Y2 - X1*Y3 + X3*Y1 + X1*Y2 - X2*Y1)   
	return A

X1 = raw_input("X1 coordinate:")
Y1 = raw_input("Y1 coordinate:")
X2 = raw_input("X2 coordinate:")
Y2 = raw_input("Y2 coordinate:")
X3 = raw_input("X3 coordinate:")
Y3 = raw_input("Y3 coordinate:")


X1 = float(X1)
Y1 = float(Y1)
X2 = float(X2)
Y2 = float(Y2)
X3 = float(X3)
Y3 = float(Y3)

print ('Area of the triangle equals:', TriangleArea(X1,Y1,X2,Y2,X3,Y3))

