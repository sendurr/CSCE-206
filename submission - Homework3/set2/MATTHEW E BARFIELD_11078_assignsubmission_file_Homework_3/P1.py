print "Question 1 - Area of a Triangle"

def area(vert):
    A = 0.5 * abs(vert[1][0] * vert[2][1] - vert[2][0] * vert[1][1] -
                  vert[0][0] * vert[2][1] + vert[2][0] * vert[0][1] +
                  vert[0][0] * vert[1][1] - vert[1][0] * vert[0][1])
    return A

v1 = (0, 0)
v2 = (1, 0)
v3 = (0, 2)
Vertices = [v1, v2, v3]
Triangle = area(Vertices)

print 'Area of the Triangle is %.2f' % Triangle