import numpy as np
import matplotlib.pyplot as plt

# infile=open("density_water.dat",'r')
# infile1=open("density_air.dat",'r')

# lines=infile.readlines()

# lines1=infile1.readlines()

# water_temp=[]
# water_density=[]

# air_temp=[]
# air_density=[]

# for x in lines:
#     if x=="\n" or x[0]=="#":
#         continue
#     try:
#         lhs,rhs=x.strip().split('   ')
#         water_density.append(rhs)
#         water_temp.append(lhs)
#     except:
#         continue

# for x in lines1:
#     if x=="\n" or x[0]=="#":
#         continue
#     try:
#         lhs,rhs=x.strip().split('     ')
#         air_density.append(rhs)
#         air_temp.append(lhs)
#     except:
#         continue


def read(d):
    data = {}
    data['temp'], data['den'] = np.loadtxt(d, unpack=True)
    return data
# print read("density_air.dat")

def fit(x, y, substance):
    plt.plot(x, y, 'o')

    for deg, linecol in [(1, '#67001f'), (2, '#006837')]:
        coeff = np.polyfit(x, y, deg)
        y_fit = np.poly1d(coeff)
        plt.plot(x, y_fit(x), '--',
                 color=linecol)

    # set axis
    x_range = x.max() - x.min()
    y_range = y.max() - y.min()
    plt.ylim([y.min() - 0.1 * y_range, y.max() + 0.1 * y_range])
    plt.xlim([x.min() - 0.1 * x_range, x.max() + 0.1 * x_range])
    plt.xlabel('Temperature (degrees Celsius)')
    plt.ylabel('Density (kg/m^3)')
    plt.title('Temperature dependence of %s Density' % substance)
    plt.legend(['data',
                'fitted 1st degree polynomial',
                'fitted 2nd degree polynomial'])
    plt.show()

# air density plot prints first
data = read('density_air.dat')
fit(data['temp'], data['den'], 'Air')

# water density plot prints second
data = read('density_water.dat')
fit(data['temp'], data['den'], 'Water')