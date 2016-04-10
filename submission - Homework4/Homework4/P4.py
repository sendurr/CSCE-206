import numpy as np

def f(x):
    s = np.sin(np.cos(x))
    return s

x = np.array([1,3,5,7,10,15])
y = f(x)
print y