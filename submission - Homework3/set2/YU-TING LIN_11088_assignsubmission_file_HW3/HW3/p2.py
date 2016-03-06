sumoddnumber=[2,5,7,4,8,3,5]
sumoddnumber.sort()

odds = []
for num in sumoddnumber:
    if num % 2 == 1:
        odds.append(num)
print odds
total = sum(odds)
print "sum=",total

