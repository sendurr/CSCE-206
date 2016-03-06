# print c; c adds the list b to the end of list a c=[1,3,5,7,11,13,17]
# print d; d adds one to every item in the list a d= [2,4,6,8,12]
# print d[-2:] prints the second to last intem to the end of the list d. which is [0,18]
a= [1,3,5,7,11]
b=[13, 17]
c= a +b
print c
b[0]=-1
d= [e+1 for e in a]
print d
d.append(b[0] +1)
d.append(b[-1] +1)
print d[-2:]

