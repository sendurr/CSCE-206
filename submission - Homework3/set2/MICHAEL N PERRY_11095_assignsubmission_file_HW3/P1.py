#P1
def Area(verticies):
	xy1=verticies[0]
	xy2=verticies[1]
	xy3=verticies[2]
	A=0.5*(xy2[0]*xy3[1]-xy3[0]*xy2[1]-xy1[0]*xy3[1]+xy3[0]*xy1[1]+xy1[0]*xy2[1]-xy2[0]*xy1[1])
	print A
coordinates=[[0,0],[1,0],[0,2]]
Area(coordinates)