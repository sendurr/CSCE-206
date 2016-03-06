#P3: generate coordinate list between 1:2:.01
coord = []
h = .01
start = 1
for i in range(101):
    coord.append(start+i*h)
print coord
print len(coord)