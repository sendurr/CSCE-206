# Jeremy Abrams
# CSCE 206
# Lab 7 - Vote.py
# February 25, 2016

infile = open("votes.txt", 'r')

lines = infile.readlines()

candidateDict = {}
for line in lines:
	candidates = line.strip().split(",")
	for candidate in candidates:
		if not candidate in candidateDict:
			candidateDict[candidate] = 1
		else:
			candidateDict[candidate] += 1

print candidateDict




