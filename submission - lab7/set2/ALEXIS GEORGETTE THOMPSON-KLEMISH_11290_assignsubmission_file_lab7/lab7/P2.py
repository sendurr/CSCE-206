filename=open("votes.txt",'r')
lines = filename.readlines()
names = []
for x in lines:
	votes = x.strip().split(",")
	for vote in votes:
		vote = vote.strip()
		names.append(vote)
candidate1 = 0
candidate2 = 0
candidate3 = 0
candidate4 = 0
candidate5 = 0
for vote in names:
	if vote.lower() == 'lilly':
		candidate1 += 1
	elif vote.lower() == 'linda':
		candidate2 += 1
	elif vote.lower() == 'john':
		candidate3 += 1
	elif vote.lower() == 'jimmy':
		candidate4 += 1
	elif vote.lower() == 'joseph':
		candidate5 += 1
tallies = [candidate1, candidate2, candidate3, candidate4, candidate5]
candidates = ['lilly', 'linda', 'john', 'jimmy', 'joseph']
for index in range(len(candidates)):
	print "%6s %6i" % (candidates[index], tallies[index])
filename.close()