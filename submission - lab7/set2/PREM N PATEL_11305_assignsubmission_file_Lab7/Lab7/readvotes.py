infile=open("votes.txt",'r')

lines = infile.readlines()
# print lines

names = []
johncount = 0
jimmycount = 0
josephcount = 0
lindacount = 0
lillycount = 0
for x in lines:
	names.append(x.strip().split(','))
print names
for group in names:
	for name in group:
		print name
		if name == 'John' or name == 'john':
			johncount += 1
		elif name == 'Jimmy' or name == 'jimmy':
			jimmycount += 1
		elif name == 'Joseph' or name == 'joseph':
			josephcount += 1
		elif name == 'linda' or name == 'Linda':
			lindacount += 1
		elif name == 'lilly' or name == 'Lilly':
			lillycount += 1

print "John: ", johncount
print "Jimmy: ", jimmycount
print "Joseph: ", josephcount
print "Linda: ", lindacount
print "Lilly: ", lillycount