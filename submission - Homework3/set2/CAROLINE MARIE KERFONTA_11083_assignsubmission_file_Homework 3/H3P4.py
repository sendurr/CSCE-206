import sys
print (sys.argv)
print ('v0=?',',','t=?')
v0= float(sys.argv[1])
t= float(sys.argv[3])
g = 9.81
y = v0*t-0.5*g*t**2

print(y)