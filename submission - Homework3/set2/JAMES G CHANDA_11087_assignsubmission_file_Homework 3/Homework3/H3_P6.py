''' modify the program p5b.py in P5 so that when user input wrong values for v0
and t, it will report an error and ask user to input it again using
raw_input function (use try-except statement)'''

print "Question 6"
import sys

try:
	v0= eval(sys.argv[1])
except IndexError:
	v0= eval(raw_input("v0=?\n"))
	print "Error: input again using raw_input function"

try:
	t=eval(sys.argv([2]))
except IndexError:
	t = eval(raw_input("t=?\n"))
	print "Error: input again using raw_input function"

g = 9.81
y = (v0*t) - (0.5*g*t**2)
print y