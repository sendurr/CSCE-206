infile=open("votes.txt",'r')

lines=infile.readlines()


johncount=0
jimmycount=0
lindacount=0

for x in lines:
	items1=x.strip()
	items2=items1.split(',')
	for x in items2:
		if x=="John":
			johncount+=1
		elif x=="Jimmy":
			jimmycount+=1
		elif x=="Linda":
			lindacount+=1		

m={'John': johncount,'Jimmy': jimmycount,'Linda':lindacount}


n=reversed(sorted(m.items(), key=lambda x:x[1]))
for x in n:
	print (x)

