import sys
try:
	C = float(sys.argv[1])
except:
	print "you failed to provide a command line arg.! "
sys.exit(1) # abort
F = 9.0*C/5 + 32
print '%gC is %.1fF' % (C, F)