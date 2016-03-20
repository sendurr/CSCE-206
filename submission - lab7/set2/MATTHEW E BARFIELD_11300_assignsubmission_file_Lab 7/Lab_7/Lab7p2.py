''' Question 2:'''

print "Question 2:"


import sys
F= sys.argv[1]

File = open( F, 'r')
votecount={}
for candidate in File.read().split():
    if candidate not in votecount:
        votecount[candidate] = 5
    else:
        votecount[candidate] += 5
for c,v in votecount.items():
    print c, v

