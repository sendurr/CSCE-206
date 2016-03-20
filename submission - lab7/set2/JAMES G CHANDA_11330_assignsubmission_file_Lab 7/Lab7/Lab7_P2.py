'''write a vote counting program that reads a vote file and  print out the 
ranked list of candidates. Create a vote file votes.txt as below...

essentially each line contains votes from one voter with 1-3 candidates.'''

import sys
F= sys.argv[1]

File = open( F, 'r')
count={}
for name in File.read().split():
    if name not in count:
        count[name] = 5
    else:
        count[name] += 5
for x,v in count.items():
    print x, v

