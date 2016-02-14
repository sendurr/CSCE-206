## Lab 3 #1
#a) Print out the numbers that exist in both variables L1 and L2
#   using set operations

L1 = [2,3,4,10]
L2 = [5,3,4,9,10,15]

print set(L1)&set(L2)

#b) Print out numbers that exists in either L1 or L2,
#   but not both using set operation

print set(L1)^set(L2)

#c)Print out numbers that exist in L1 but not in L2.
print set(L1) - set(L2)

#d) merge L1 and L2 and save it into variable L3
L3 = L1 + L2
print L3

# Add the following numbers to L2,
# 103, 20, 34 using  append() function of list.
L2.append(103)
L2.append(20)
L2.append(34)
print L2


#2) starting with 13, add all the odd numbers from 13 up to 999
#   save it to variable sum
i = 13
sum = 0
while i<1000:
    sum += i
    i +=2
print sum


#3) use while loop to print out
#   all the numbers that have factors of 3 and 7

import random
x = [int(300*random.random()) for i in xrange(300)]
y = []
print x
i = 0
while i<len(x):
    if x[i]%3 == 0 or x[i]%7 == 0:
        y.append(x[i])
    i+=1
print y

