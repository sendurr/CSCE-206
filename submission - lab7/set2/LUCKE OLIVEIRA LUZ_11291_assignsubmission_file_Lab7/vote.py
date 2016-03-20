import sys

infile = open(sys.argv[1],'r')

votes = infile.readlines()

Carl = 0
John = 0
Jimmy = 0

for i in votes:
	j = i.strip().split(",")
	for k in j:
		if k == "Carl":
			Carl += 1
		elif k == "John":
			John += 1
		elif k == "Jimmy":
			Jimmy += 1

total = {"Carl":Carl,"John":John,"Jimmy":Jimmy}

for candidate in sorted(total, key=total.get, reverse=True):
	print candidate, total[candidate]