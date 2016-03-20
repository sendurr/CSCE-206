infile=open("votes.txt",'r')
lines=infile.readlines()
print lines
wordcount={}
for x in lines:
	votes=x.strip()
	print votes
	if x not in wordcount:
		wordcount[x]=1
	else:
		wordcount[x]+=1
for k,v in wordcount.items():
	print k,v