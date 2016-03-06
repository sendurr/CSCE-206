def area_of_polygon(vertices):
    (x1, y1), (x2, y2), (x3, y3) = vertices
    return abs(x1 * y2 + x2 * y3 + x3 * y1 - y1 * x2 - y2 * x3 - y3 * x1) / 2
def lop_triangle(vertices):
    triangle = [vertices[0], vertices[-1], vertices[-2]]
    polygon = vertices[:-1]
    return triangle, polygon
def area_of_triangle(vertices):
    if len(vertices) == 3:
        return area_of_polygon(vertices)
    else:
        triangle, polygon = lop_triangle(vertices)
        return area_of_triangle(triangle) + area_of_polygon(polygon)
print(area_of_triangle([[0,0],[1,0],[0,2]]))