file=open("votes.txt")
wordcount={}
for John in file.read().split():
    if John not in wordcount:
        wordcount[John] = 1
    else:
        wordcount[John] += 1
for Lilly in file.read().split():
    if Lilly not in wordcount:
        wordcount[Lilly] = 1
    else:
        wordcount[Lilly] += 1
for Linda in file.read().split():
    if Linda not in wordcount:
        wordcount[Linda] = 1
    else:
        wordcount[Linda] += 1
for j in wordcount.items():
    print j



