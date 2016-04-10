'''################################################################################
    CSCE 206 Homework4  , Exercise Q2
    plot a graph fir exp(x^2) sin(x)
    
    Author:   Sendurr Selvaraj
    Email:    sendurr@hotmail.com
################################################################################'''

from numpy import *
from matplotlib.pyplot import *

x=arange(-3.14,3.14,0.01)
y=(exp(x**2))*sin(x)
plot(x,y)
legend (["y=(exp(x**2))*sin(x)"])
xlabel("x")
ylabel("y")
title('Grap for x vs y')
show()

'''################################################################################
    End of Program
################################################################################'''
