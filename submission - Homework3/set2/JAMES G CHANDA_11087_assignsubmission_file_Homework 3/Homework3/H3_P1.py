''' Question 1: finding the area of a triangle'''

def area(vertices):
    xy_1 = vertices[0]
    xy_2 = vertices[1]
    xy_3 = vertices[2]

    A = 0.5 * (xy_2[0]*xy_3[1] - xy_3[0]*xy_2[1] - xy_1[0]*xy_3[1] + xy_3[0]*xy_1[1] + xy_1[0]*xy_2[1] - xy_2[0]*xy_1[1])
    return A

AreaofTraingle = [[0,0], [1,0], [0,2]]

print area(AreaofTraingle)