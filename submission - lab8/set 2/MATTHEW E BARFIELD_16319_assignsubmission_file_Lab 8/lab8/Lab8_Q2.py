import numpy as np
import matplotlib.pyplot as plt


def load(densityfile):
    data = {}
    data['Temperature'], data['Density'] = np.loadtxt(densityfile, unpack=True)
    return data


def fit(x, y, substance):
    plt.plot(x, y, 'o',
            size=8,
            width=1.5,

    for deg, linecol in [(1, '#67001f'), (2, '#006837')]):
        coeff = np.polyfit(x, y, deg)
        y_fit = np.poly1d(coeff)
        plt.plot(x, y_fit(x), '--',
                 color=linecol)

    x_range = x.max()-x.min()
    y_range = y.max()-y.min()
    plt.xlim([x.min()-0.1 * x_range, x.max() + 0.1 * x_range])
    plt.ylim([y.min()-0.1 * y_range, y.max() + 0.1 * y_range])
    plt.xlabel('Temperature')
    plt.ylabel('Density')
    plt.title('Temperature Dependence of %s Density' % substance)
    
    plt.show()

data = load('Density_air.dat')
fit(data['Temperature'], data['Density'], 'Air')


data = load('Density_water.dat')
fit(data['Temperature'], data['Density'], 'Water')