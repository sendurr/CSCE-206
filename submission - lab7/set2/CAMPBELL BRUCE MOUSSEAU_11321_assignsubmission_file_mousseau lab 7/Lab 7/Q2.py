import from file("votes.txt")
votecount={}

for Linda in file.read().split():
    if Linda not in votecount:
        votecount[Linda] = 1
    else:
        votecount[Linda] += 1

for John in file.read().split():
    if John not in votecount:
        votecount[John] = 1
    else:
        votecount[John] += 1

for Lilly in file.read().split():
    if Lilly not in votecount:
        votecount[Lilly] = 1
    else:
        votecount[Lilly] += 1

print (votecount)
