#Lab 7
#6 March 2016

#Question 2

import operator

infile = open('votes.txt', 'r')
lines = infile.readlines()
Candidates = set()
for x in lines:
	items=x.strip().split(",")
	for i in items:
		Candidates.add(i)
d = dict.fromkeys(list(Candidates),0)

for x in lines:
	items=x.strip().split(",")
	for i in items:
		d[i]+=1

import operator
sorted_x = sorted(d.items(), key=operator.itemgetter(1), reverse = True)
for x in sorted_x:
	print x[0],"\t",x[1]