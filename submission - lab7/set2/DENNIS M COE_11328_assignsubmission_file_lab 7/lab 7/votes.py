from collections import Counter

infile = open("votes.txt", 'r')
	
lines = infile.readlines()
new_ls = []

for i in lines:
	i = i.split(" ", 3)
	for j in i:
		new_ls.append(j)

thelist = [(i.rstrip('\n')).rstrip(',') for i in new_ls]

for i in thelist:
	counts = Counter(thelist)

print counts
