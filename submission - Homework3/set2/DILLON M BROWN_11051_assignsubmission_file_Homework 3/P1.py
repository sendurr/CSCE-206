def area(coor):
    x = []
    y = []
    if len(coor) == 3:
        for i in xrange(3):
            if len(coor[i]) == 2:
                x.append(coor[i][0])
                y.append(coor[i][1])
                continue
            return "Error: Program accepts 2D coordinates"
    else:
        return 'Error: Please enter 3 sets of coordinates'
    tria = 0.5*((x[0]-x[2])*(y[1]-y[0])-(x[0]-x[1])*(y[2]-y[0]))
    return tria

test = [[0,0],[1,0],[0,2]]
print 'Area of triangle is %.3f'%(area(test))
