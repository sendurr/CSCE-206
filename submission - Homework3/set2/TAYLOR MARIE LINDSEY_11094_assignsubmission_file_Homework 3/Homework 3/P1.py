
import math

def area (vertices):
    xy=[]
for pair in vertices:
    for i in pair:
        xy.append(i)
x1=xy[0]
y1=xy[1]
x2=xy[2]
y2=xy[3]
x3=xy[4]
y3=xy[5]

A=0.5*math.abs((x2*y3)-(x3*y2)-(x1*y3)+(x3*y1)+(x1*y2)-(x2*y1))

return A
print area ([0,0],[1,0],[0,2])