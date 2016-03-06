
import sys

print sys.argv
if len(sys.argv)-1 >=3:
	print "enter only two parameters: v0 and t"
sys.exit()
g=9.81
v=float(sys.argv[1])
t=float(sys.argv[2])

y=v0*t-0.5*g*t**2
print 'y:',y