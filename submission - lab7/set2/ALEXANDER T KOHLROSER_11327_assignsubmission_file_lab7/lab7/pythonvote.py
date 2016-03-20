file = open("votes.txt", 'r')

lines = file.readlines()

john = 0
jimmy = 0
lilly = 0
joseph = 0
linda = 0

people = ['John', 'Jimmy', 'Lilly', 'Joseph', 'Linda']

All = []

for x in lines:
	votes = x.strip().split(",")

	for vote in votes:
		vote = vote.strip()
		All.append(vote)

for vote in All:
	if vote.lower() == 'john':
		john += 1

	elif vote.lower() == 'jimmy':
		jimmy += 1

	elif vote.lower() == 'lilly':
		lilly += 1

	elif vote.lower() == 'joesph':
		joseph += 1

	elif vote.lower() == 'linda':
		linda += 1

count = [john, jimmy, lilly, joseph, linda]

for i in range(len(people)):
	print "%6s %6i" % (people[i], count[i])

file.close()