import numpy as np
import matplotlib.pyplot as plt


def load(densityfile):
    data={}
    data['temp'], data['density']=np.loadtxt(densityfile, unpack=True)
    return data


def fit(x, y, substance):
    plt.plot(x, y, 'o', markerfacecolor='#2166ac', markeredgecolor='#053061', markersize=8, markeredgewidth=1.5)

    for deg, linecol in [(1, '#67001f'), (2, '#006837')]:
        coeff=np.polyfit(x, y, deg)
        y_fit=np.poly1d(coeff)
        plt.plot(x, y_fit(x), '--', color=linecol)

    x_range=x.max()-x.min()
    y_range=y.max()-y.min()
    plt.xlim([x.min()-0.1*x_range, x.max()+0.1*x_range])
    plt.ylim([y.min()-0.1*y_range, y.max()+0.1*y_range])
    plt.xlabel('Temp')
    plt.ylabel('Density')
    plt.title('Temp dependence of %s density' % substance)
    plt.legend(['data', 'fitted degree 1 polynomial', 'fitted degree 2 polynomial'])
    plt.show()

data=load('density_air.dat')
fit(data['temp'], data['density'], 'air')

data=load('density_water.dat')
fit(data['temp'], data['density'], 'water')