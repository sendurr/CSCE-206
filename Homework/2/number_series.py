'''################################################################################
        CSCE 206 Homework - 2 , Exercise P1
                Number Series
                        
                Author:   Sendurr Selvaraj
                Email:    sendurr@hotmail.com
################################################################################'''




result= [1,0]
prev1=0
prev2=1

for x in range (1,999):
	current = prev1 + prev2
	result.append(current)
	if (current >=1000):
	prev1 = prev2
	prev2 = current

print result
print len(result)

'''################################################################################
        End of Program
################################################################################'''
