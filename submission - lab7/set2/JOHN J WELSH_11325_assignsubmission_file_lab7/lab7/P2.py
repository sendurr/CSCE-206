infile=open("votes.txt",'r')

lines = infile.readlines()

john, jimmy, lilly, linda, joseph = 0, 0, 0, 0, 0
candidates = ['john', 'jimmy', 'lilly', 'linda', 'joseph']
allvotes = []

for x in lines:
	votes = x.strip().split(",")
	for vote in votes:
		vote = vote.strip()
		allvotes.append(vote)

for vote in allvotes:
	if vote.lower() == 'john':
		john += 1
	elif vote.lower() == 'jimmy':
		jimmy += 1
	elif vote.lower() == 'lilly':
		lilly += 1
	elif vote.lower() == 'linda':
		linda += 1
	elif vote.lower() == 'joseph':
		joseph += 1

votecount = [john, jimmy, lilly, linda, joseph]

for index in range(len(candidates)):
	print "%6s %6i" % (candidates[index], votecount[index])

infile.close()