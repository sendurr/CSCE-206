from numpy import *
import matplotlib.pyplot as plt

def f(x):
    ans = exp(x**2)*sin(x)
    return ans

x = linspace(-3.14,3.14,51)
d=f(x)
plt.plot(x,d)
plt.xlabel('x')
plt.ylabel('y')
plt.legend('f(x)')
plt.title('P2')
plt.show()