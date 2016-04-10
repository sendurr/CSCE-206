'''################################################################################
    CSCE 206 Homework4  , Exercise Q3
    plot a formula for several parameters
    
    Author:   Sendurr Selvaraj
    Email:    sendurr@hotmail.com
################################################################################'''

from numpy import *
from matplotlib.pyplot import *
import sys
g = 9.81
legends=[]
for i in range(1,len(sys.argv)):
	v0 = float(sys.argv[i])
	t_max = 2*v0/g
	t = linspace(0,2*v0/g)
	y = (v0*t) -0.5*g*(t**2)
	hold(True)
	plot(t,y, label=('v0=%g'%v0))
legend(loc='upper left')
xlabel("t")
ylabel("y(t)")
title('Grap for y(t) vs t')
show()

'''################################################################################
    End of Program
################################################################################'''
