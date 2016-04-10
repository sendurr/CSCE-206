from matplotlib.pylab import *

# Define the function to plot
def f(x):
	return (exp(x**2))*sin(x)

# define the range of the plot
x = arange(-3.14,3.14,0.01) 
y = zeros(len(x)) 

# define the function within the range of the plot
for i in xrange(len(x)):
	y[i] = f(x[i])

plot(x, y)
show()