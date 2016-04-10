g=9.81

def f(t):
	return v0*t-0.5*g*t**2
def f_vectorized(t):
	x1 = <t=0>
	x2 = <t=2*v0/g>
	r = np.where(condition, x1, x2)
	return r 

t = linspace(0, 2*v0/g)
y1 = f(t)
y2 = f_vectorized(t)

plot(t, y1, 'r-')
hold('on')
plot(t, y2, 'bo')
xlabel('t')
ylabel('y')
legend(['f(t)'], 'f_vectorized(t)')
title('homework 4')
show()