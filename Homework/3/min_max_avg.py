'''################################################################################
    CSCE 206 Homework - 3 , Exercise P3
        Minium , Maximum and Average
             
        Author:   Sendurr Selvaraj
        Email:    sendurr@hotmail.com
################################################################################'''
 
def minmaxave(list):
	min=list[0]
	max=list[0]
	sum=0
	result = []
	for i in list:
		sum= sum + i
		if(i> max):
			max=i
		if(i<min):
			min=i
	avg=sum/len(list)
	result.append(min)
	result.append(max)
	result.append(avg)
	return result



list =[3,5,2.3,5,10,4.2]
result=[]
result = minmaxave(list)
print("The Minimum number is " + str(result[0]) + "\n")
print("The Maximum number is " + str(result[1]) + "\n")
print("The Average of the numbers is " + str(result[2]) + "\n")


 
'''################################################################################
    End of Program
################################################################################'''

