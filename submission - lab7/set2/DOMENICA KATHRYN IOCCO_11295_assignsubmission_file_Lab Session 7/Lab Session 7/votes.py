#Question 2--------------------
import operator
inputfile=open("votes.txt",'r')
vote=inputfile.readlines()
inputfile.close()
dictionary={}
for lines in vote:
	line = lines.strip().split(",")
	for name in line:
		if name.strip() not in dictionary:
			dictionary[name.strip()]=1
		else:
			dictionary[name.strip()]+=1
print(dictionary)
sorted_dictionary=sorted(dictionary.items(),
	key=operator.itemgetter(1), reverse=True)
for z in sorted_dictionary:
	print(z[0], "\t", z[1])
