'''################################################################################
        CSCE 206 LAB - 3
                Lab -3 : play with list and set
                        
                Author:   Sendurr Selvaraj
                Email:    sendurr@hotmail.com
################################################################################'''

'''################################################################################
        inter_funct
               Returns the elements with are not in the second set
################################################################################'''

def inter_funct(set1 , set2):


        result=[]
        for x in set1:
            match="no"
            for y in set2:
                if (x == y):
                    match="yes"
                    break
            if (match == "no"):
                result.append(x)

        return result

'''################################################################################
        End of method
################################################################################'''

# 1. play with list and set

# L1=[2, 3, 4,10]
# L2=[5,3,4,9,10,15]

# Print out the numbers that exist in both variables L1 and L2 using set operations

# Print out numbers that exists in either L1 or L2, but not both using set operation

# Print out numbers that exist in L1 but not in L2. 

# merge L1 and L2 and save it into variable L3

# Add the following numbers to L2,   103, 20, 34 using  append() function of list.

L1=set([2, 3, 4,10])
L2=set([5,3,4,9,10,15])

print "The numbers that exist in both variables L1 and L2 are " + str(L1.intersection(L2))

result = (inter_funct(L1,L2)) + (inter_funct(L2,L1))

print "The numbers that exists in either L1 or L2 are " + str(result)

result = (inter_funct(L1,L2))

print "The numbers that exist in L1 but not in L2 are " + str(result)

L3 = L1.union(L2)

print " The merger of L1  + L2 = L3 = " + str(L3)

result=[]

for x in L2:
        result.append(x)

result.append(103)
result.append(20)
result.append(34)

print " After adding 103, 20, 34 using  append() function of list : " + str(result)


# 2. while loop application

# starting with 13, add all the odd numbers from 13 up to 999
# save it to variable sum

x=13
var_sum=0

while (x <= 999):
    if (x % 2 != 0):
        var_sum +=x
    x = x+1 

print "The sum of odd numbers between 13 and 99 is " + str(var_sum)


# 3. The following code generates 300 random integers
# use while loop to print out all the numbers that have factors of 3 and 7
# hint: use % operator


import random
x=[int(300*random.random()) for i in xrange(300)]

result = []
i=0
while(i<len(x)):
    if( (x[i]%3 == 0) & (x[i]%7 ==0)):
        result.append(x[i])
    i+=1

print "The list of random numbers which are a factor of 3 & 7 are " + str(result)


'''################################################################################
        End of Program
################################################################################'''
