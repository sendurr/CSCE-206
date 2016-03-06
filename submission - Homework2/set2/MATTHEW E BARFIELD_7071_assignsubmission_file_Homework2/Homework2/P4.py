
A=[1,2,5,7,11]
B=[13,17]
C=A+B
print C
print 'This prints the appended lists of A and B'
print ''

B[0]=-1
D=[E+1 for E in A]
print D
print 'This prints the values of A, each value being increased by 1'
print ''

D.append(B[0]+1)
D.append(B[-1]+1)
print D[-2:]
print 'This prints the extremes of C, made more extreme by a value of 1'