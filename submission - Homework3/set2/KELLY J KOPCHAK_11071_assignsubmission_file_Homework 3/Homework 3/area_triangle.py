V1=(0,0)
V2=(1,0)
V3=(0,2)
Verticies=[V1,V2,V3]

def f(V1,V2,V3):
	area=.5*(V2[0]*V3[1]-V3[0]*V2[1]-V1[0]*V3[1]+V3[0]*V1[1]+V1[0]*V2[1]-V2[0]*V1[1])
	return area
print f([0,0],[1,0],[0,2])

