# Kate Shereyk
from numpy import *
from matplotlib.pyplot import *
import sys

if len(sys.argv) ==1:
    print 'v0 values from command line'
    sys.exit(1)

v0_list = [float(v0) for v0 in sys.argv[1:]]
g = 9.81 #gravity

legends = [] 
for v0 in v0_list:
    v0 = float(v0)
    t_max = 2*v0/g
    t = linspace(0,t_max,100)
    y = v0*t -0.5*g*t**2
    hold(True)
    plot(t,y)
    legends.append('v0=%g'%v0)


xlabel('seconds')
ylabel('meters')
legend(legends)
show()
