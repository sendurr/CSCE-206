q=(('a','b','c'),('d','e','f'),('g','h'))
print q[0][0]
print q[1]
print q[2][1]
print q[1][0]
#print q[-1][-2]
#g q[-1][-2] has the value g because the index starts at 0, meaning -1 will go backwards and give us the las tindex, and -2 will go backwards 2 spaces within ('g','h'), giving us g.