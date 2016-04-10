from numpy import*
import matplotlib.pyplot as plt

def F(x):
	answer=exp(x**2)*sin(x)
	return answer

xlist=linspace(-3.14,3.14,51)

plt.plot(xlist, F(xlist))
plt.xlabel('x')
plt.ylabel('y')
plt.legend('f(x)=exp(x^2)*sin(x)')
plt.title('Problem 2')
plt.show()