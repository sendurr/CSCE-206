'''################################################################################
        CSCE 206 Homework - 2 , Exercise P4
                acceleration table
                        
                Author:   Sendurr Selvaraj
                Email:    sendurr@hotmail.com
################################################################################'''




a = [1,3,5,7,11]
b=[13 , 17]

c=a+b
print c
print "print c"
print"This prints the concatenation of list a and b"

b[0] = -1
print"b[0] = -1"
print "This assigns 1st element of b with -1"

d=[e+1 for e in a]
print"d=[e+1 for e in a]"
print"This loops all elements in a and assigns the elements to b with an increment by 1"

d.append(b[0] +1)
print"d.append(b[0] +1) - This takes the 1st element of b and adds with 1 and appends as last element to b"
d.append (b[-1] +1)
print"d.append (b[-1] +1) - This takes the last element of b and adds with 1 and appends as last element to b"
print d[-2:]
print "print d[-2:] : This prints the last two elements of d";

'''################################################################################
        End of Program
################################################################################'''
