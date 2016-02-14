q= [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]
print q[0][0]
print q[1]
print q[2][1]
print q[1][0]
print q[-1][-2]
print " The first number assigned starts from 0, but if a negative numner is assigned, python reads it backward. So, in q[-1] means one row before row 0 will be the answer which is row 3 [g,h]. Then, q[-1][-2] means that find the second number counting backward in row 3. The [0] means g in row 3 when counting backward h becomes -1 and g is -2. "