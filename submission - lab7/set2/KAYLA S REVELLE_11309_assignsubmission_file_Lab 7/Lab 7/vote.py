from collections import Counter

infile = open('votes.txt', 'r')

vote = infile.readlines()
list1 = []

for x in vote:
	x = x.split(' ', 3)
	for i in x:
		list1.append(i)

number = [(x.rstrip('\n')).rstrip(',') for x in list1]

for n in number:
	rank = Counter(number)

print (rank)