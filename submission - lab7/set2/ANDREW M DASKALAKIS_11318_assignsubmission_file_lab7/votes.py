

infile = open('votes.txt','r')
lines = infile.readlines() #loads into list
infile.close()

vJohn = 0
vLilly = 0
vLinda = 0

for line in lines:
	l1 = line.strip()
	l2 = l1.split(",")
	for x in l2:
		if x == "John":
			vJohn +=1
		elif x == "Lilly":
			vLilly +=1
		elif x == "Linda":
			vLinda +=1

print "John %d"%vJohn
print "Lilly %d"%vLilly
print "Linda %d"%vLinda