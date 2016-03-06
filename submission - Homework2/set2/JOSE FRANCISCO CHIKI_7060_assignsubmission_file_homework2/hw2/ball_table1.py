def y(t):
	return (1*t)-(.5*9.81)*(t**2)
for i in range(0,int(((2*1)/9)),(((2*1)/9)/11)):
	print t, "\t", y(t)
	# i am given "TypeError: range() integer end argument expected, got float." when i print, but the range ends with a non-integer
# for i in range(0,int(((2*1)/9.81)),((((2*1)/9.81)/11))):
# this results in the same error, only now it says that the step argument needs to be an integer, which it cannot be in this situation
