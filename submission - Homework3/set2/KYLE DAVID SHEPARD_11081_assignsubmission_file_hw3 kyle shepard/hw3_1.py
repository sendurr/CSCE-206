def area(vertices):
    xy1=vertices[0]
    xy2=vertices[1]
    xy3=vertices[2]
    area=0.5*(xy2[0]*xy3[1]-xy3[0]*xy2[1]-xy1[0]*xy3[1]+xy3[0]*xy1[1]+xy1[0]*xy2[1]-xy2[0]*xy1[1])
    return area
triangle=[[0,0],[1,0],[0,2]]
print area(triangle)