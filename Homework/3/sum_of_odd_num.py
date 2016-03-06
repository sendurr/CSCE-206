'''################################################################################
    CSCE 206 Homework - 3 , Exercise P2
        sum of odd numbers
             
        Author:   Sendurr Selvaraj
        Email:    sendurr@hotmail.com
################################################################################'''
 
def sumoddnumber(list):
	sum =0
	for i in list:
		if (i%2 != 0):
			sum=sum+i
	print ("The sum of odd numbers is =  " + str(sum))



list =[2,5,7,4,8,3,5]
sumoddnumber(list)

 
'''################################################################################
    End of Program
################################################################################'''

