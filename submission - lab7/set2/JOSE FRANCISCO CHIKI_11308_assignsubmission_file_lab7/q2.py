infile=open("votes.txt","r")
votes=[]
john=[]
josh=[]
linda=[]
for x in infile:
	items=x.strip("\n").split(",")
	try:
		votes.append(items)
	except:
		continue
totalvotes=votes[0]+votes[1]+votes[2]
josh.append(totalvotes.count('josh'))
john.append(totalvotes.count('john'))
linda.append(totalvotes.count('linda'))
print "John",john
print "Josh",josh
print "Linda",linda