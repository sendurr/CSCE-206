'''################################################################################
        CSCE 206 Homework - 1 , Question 6
                Set operations
                        
                Author:   Sendurr Selvaraj
                Email:    sendurr@hotmail.com
################################################################################'''

X= set([1, 3, 8, 10, 14, 10, 20, 25])
Y=set([3,3,8,10,15,20,33,55,88])

print "The union of set X|Y = " + str(X|Y)
print "The intersection of set X&Y = " + str(X&Y)
print "X-Y = " + str(X.difference(Y))
print "Y-X = " + str(Y.difference(X))


'''################################################################################
        End of Program
################################################################################'''
