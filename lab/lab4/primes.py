'''################################################################################
        CSCE 206 Lab - 4 , Exercise P1
                Work with list
                        
                Author:   Sendurr Selvaraj
                Email:    sendurr@hotmail.com
################################################################################'''




ini_list =[2 ,3 , 5 ,  7 ,  11 , 13]
temp_list = []
final_list=[]
p=17

for i in ini_list:
	temp_list.append(i)

final_list = temp_list
final_list.append(p)
print(" Initial List = " + str(ini_list) + "\n")
print(" Final List = " + str(final_list) + "\n")



'''################################################################################
        End of Program
################################################################################'''
