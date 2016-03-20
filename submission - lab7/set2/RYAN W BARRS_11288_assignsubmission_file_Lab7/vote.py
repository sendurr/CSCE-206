import re
from collections import Counter

file=open('votes.txt','r')
candidates = re.findall(r'\w+', file.read())
votes = Counter(candidates)
print votes