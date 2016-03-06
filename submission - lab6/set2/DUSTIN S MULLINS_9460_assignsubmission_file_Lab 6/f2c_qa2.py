#2.
import sys
print sys.argv

if len(sys.argv)-1 !=1:
	print "usage: python %s is fardegree" %sys.argv[0]
	sys.exit()

F = float(sys.argv[1])
C = (F-32)*(5/9.0)
print "C:",C