#Rachel Smoak
#27 March 2016
#Homework 4

#Question 3
import sys
import numpy as np
import matplotlib.pyplot as plt

length = len(sys.argv)
v0 = []

m = 1
while m <= length-1:
	try:
		vo = float(sys.argv[m])	
		v0.append(float(sys.argv[m]))
		m+=1
	except:
		print "Please enter numeric values for all times"
		sys.exit(0)

dct={}
dct2={}
for i in v0:
	dct['%s' % i] = []
	dct2['%s' % i] = []

i = 0
g = 9.81
for key in dct:
	t = np.arange(0, 2*float(key)/g, 0.01)
	dct[key]=t

for key, val in dct.items():
	dct2[key] = float(key)*val-0.5*g*val**2

x = list(dct.values())
y = list(dct2.values())

for key in dct and dct2:
	x = list(dct[key])
	y = list(dct2[key])
	plt.plot(x,y)
	hold=True

plt.legend(dct.keys(), title='Vo (m/s)')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.show()