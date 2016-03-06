import sys

if len(sys.argv)-1 >= 3:
	print "Enter two velocity and time parameters: v0 and t"
sys.exit()
v = float(sys.argv[1])
t = float(sys.argv[2])
g = 9.81
y = ((v0 * t) - (.5 * g * t**2))
print 'y =',y



