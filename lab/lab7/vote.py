'''################################################################################
    CSCE 206 Lab7  , Exercise Q2
    Vote list report
    
    Author:   Sendurr Selvaraj
    Email:    sendurr@hotmail.com
################################################################################'''

import sys

user_file = str(sys.argv[1])

input_file=open(user_file,'r')
lines=input_file.readlines()
print

v1  = v2 = v3 = v4 = v5 =0

for x in lines:
    voters=x.strip().split(",")
    for name in voters:
        name = name.upper() # convert all voters to uppercase
        name = name.strip() # remove extra whitespaces
        if (name == "JOHN"):
            v1 = v1 + 1
        elif (name == "JIMMY"):
            v2 = v2 + 1
        elif (name == "LILLY"):
            v3 = v3 + 1
        elif (name == "LINDA"):
            v4 = v4 + 1
        elif (name == "JOSEPH"):
            v5 = v5 + 1
        else:
            print("Voter " + name + " not present in the voter list \n")

# print the no of votes.
print ("Printing the no of vote \n")

print ("John  = " + str(v1))
print ("Jimmy  = " + str(v2))
print ("Lilly  = " + str(v3))
print ("Linda  = " + str(v4))
print ("Joseph  = " + str(v5))




'''################################################################################
    End of Program
################################################################################'''

