import sys

print sys.argv
F = float(sys.argv[1])

C = (F - 32)*float(5)/9

print (C, "Degrees Celcius")