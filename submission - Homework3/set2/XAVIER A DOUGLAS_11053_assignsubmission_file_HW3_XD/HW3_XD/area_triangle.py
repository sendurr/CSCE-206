

def area(*arg):
	x2y3 = area[1][0]*area[2][1]
	x3y2 = area[2][0]*area[1][1]
	x1y3 = area[0][0]*area[2][1]
	x3y1 = area[2][0]*area[0][1]
	x1y2 = area[0][0]*area[1][1]
	x2y1 = area[1][0]*area[0][1]
	print 0.5*(x2y3 - x3y2 - x1y3 + x3y1 + x1y2 - x2y1)
print area[[0,0],[1,0],[0,2]]