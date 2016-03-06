def area(x1,y1,x2,y2,x3,y3):
	return .5*abs((x2*y3)-(x3*y2)-(x1*y3)+(x3*y1)+(x1*y2)-(x2*y1))
print area(0,0,1,0,0,2)