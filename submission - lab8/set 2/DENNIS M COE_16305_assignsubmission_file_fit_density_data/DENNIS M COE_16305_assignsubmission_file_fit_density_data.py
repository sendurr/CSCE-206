import numpy as np
import matplotlib.pyplot as plt

def loading1(density_water):
    data = {}
    data['temperature'], data['density'] = np.loadtxt(density_water, unpack=True)
    return data

def loading2(density_air):
    data = {}
    data['temperature'], data['density'] = np.loadtxt(density_air, unpack=True)
    return data

def fit(x, y, substance):
    plt.plot(x, y, 'o',
           )

    for deg, linecol in [(1, '#67001f'), (2, '#006837')]:
        coeff = np.polyfit(x, y, deg)
        y_fit = np.poly1d(coeff)
        plt.plot(x, y_fit(x), '--',
        )


    plt.xlabel('Temperature')
    plt.ylabel('Density')
    plt.title('Temperature dependence of %s density' % substance)
    plt.legend(['data',
                'fitted degree 1 polynomial',
                'fitted degree 2 polynomial']
                )
    plt.show()

data = loading1('density_air.dat')
fit(data['temperature'], data['density'], 'air')

data = loading2('density_water.dat')
fit(data['temperature'], data['density'], 'water')