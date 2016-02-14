import random
i=0
x=[int(300*random.random()) for i in xrange(300)]
while i<=299:
 if x[i]%3==0 & x[i]%7==0:
  print i
 i=i+1