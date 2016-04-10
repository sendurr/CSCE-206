#lab 8
import matplotlib.pyplot as plt
import numpy as np

def loaded(densityfiles):
    data = {}
    data['temperature'], data['density'] = np.loadtxt(densityfiles, unpack=True)
    return data

def bestfit(x, y, substance):
    plt.plot(x, y, 'o',
             markerfacecolor='#2166ac',
             markeredgecolor='#053061',
             markersize=8,
             markeredgewidth=1.5)

    for deg, linecol in [(1, '#67001f'), (2, '#006837')]:
        coeff = np.polyfit(x, y, deg)
        y_fit = np.poly1d(coeff)
        plt.plot(x, y_fit(x), '--',
                 color=linecol)

    xrange1 = x.max()-x.min()
    yrange1 = y.max()-y.min()
    plt.xlim([x.min()-0.1*xrange1, x.max()+0.1*xrange1])
    plt.ylim([y.min()-0.1*yrange1, y.max()+0.1*yrange1])
    plt.xlabel('Temperature')
    plt.ylabel('Density')
    plt.title('Temperature dependence of %s density' % substance)
    plt.legend(['data',
                'fitted degree 1 polynomial',
                'fitted degree 2 polynomial'])
    plt.show()

data = loaded('density_air.dat')
bestfit(data['temperature'], data['density'], 'air')

data = loaded('density_water.dat')
bestfit(data['temperature'], data['density'], 'water')