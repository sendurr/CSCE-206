#Question 4

CityT = {'Columbia':'82', 'Raleigh':'75', 'New York City':'68', 
'Charlotte':'78', 'Miami':'92', 'San Francisco':'83', 'Houston':'88',
'Baltimore':'69', 'Atlanta':'76', 'Nashville':'80'}

import operator
sorted_x = sorted(CityT.items(), key=operator.itemgetter(1))
for x in sorted_x:
	print (x[0], "\t", x[1])