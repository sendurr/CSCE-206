infile=open("votes.txt","r")
linesread=infile.readlines()
infile.close()

import operator

votecount={}

for lines in linesread:
	votes=lines.strip().split(",")
	for vote in votes: #try(+=1)
		try:
			votecount[vote.strip()]+=1 
			 
		except: #except(=1)
			votecount[vote.strip()]=1  #if it exists
print votecount
sorted_votecount=sorted(votecount.items(),key=operator.itemgetter(1),reverse=True)
for x in sorted_votecount:
	print(x[0],"\t",x[1])
		



	