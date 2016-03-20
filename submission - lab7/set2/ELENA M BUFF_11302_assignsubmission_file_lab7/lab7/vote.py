import sys
infile=open(sys.argv[1],'r')

lines=infile.readlines()
# print lines

votes=[]
votecount={}

# for x in lines:
# 	items=x.strip().split(",")
# 	votes.insert(0,items)
# 	# print votes
#     if x in votecount:
#         votecount[x]+=1
#     else:
#         votecount[x]=1

# for k,v in votecount.items():
#     print k,v

for x in lines:
    b=x.strip().split(",")
    votes.append(b)

# print len(votes)

l=len(votes)

while l>0:
	if x not in votecount:
		votecount[x]=1
	else:
		votecount[x]+=1
	l-=1


# for y,z in votecount.items():
#     print y,z

import operator
sorted_x=sorted(votecount.items(), key=operator.itemgetter(0))
for x in sorted_x:
	print x[0],"\t",x[1]
