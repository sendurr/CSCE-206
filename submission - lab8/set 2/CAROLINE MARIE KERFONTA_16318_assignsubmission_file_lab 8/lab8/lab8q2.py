coeff = polyfit(x, y, deg)
p = poly1d(coeff)
print (p)
y_fitted = p(x)
plot(x, y, '-r', x, y_fitted, '-b')
	lengend=('data', 'density of air to temperature')

coeff = polyfit(x, y, deg)
t = poly1d(coeff)
print (t)
y_fitted = p(x)
plot(x, y, '-r', x, y_fitted, '-b')
	lengend=('data', 'density of water to temperature')

