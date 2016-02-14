'''################################################################################
        CSCE 206 Homework - 1 , Exercise 2.19
                Nexted List 
                        
                Author:   Sendurr Selvaraj
                Email:    sendurr@hotmail.com
################################################################################'''

# Index the nested list to get
# 1) The letter a
# 2) The list ['d', 'e', 'f']
# 3) The last element
# 4) The d element

q = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]

# 1)
print q[0][0]

# 2)
print q[1]

# 3)
print q[-1][-1]

# 4)
print q[1][0]

print "Explain why q[-1][-2] is the value g? \n"
print "Answer : With - we just move left instead of the conventional  right. So we move to the last element with [-1],"
print "and in that element we move to the left twice. And with a list containing only two elements,"
print "the result will be that [-2] is the same as [0] "



'''################################################################################
        End of Program
################################################################################'''