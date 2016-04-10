
import Tkinter as tk
print tk

x= eval(tk.x)
y=eval(tk.y)

op=tk.op

print x, op, y, '='

if op=="*":
	print x*y
elif op=="-":
	print x-y
elif op=="+":
	print x+y
elif op=="/":
	if y==0:
		print "error: y=0"
	else:
		print x/y

