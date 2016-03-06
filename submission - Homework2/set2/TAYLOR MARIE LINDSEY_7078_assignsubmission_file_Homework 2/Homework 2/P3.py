i=1

coordinate = []
x = 1+i*0.01
y = 0
while y < 100:
    while 1< x < 2:
        coordinate.append((x,y))
        x += 1
    coordinate.append((x,y))
    y += 1
print(coordinate)
