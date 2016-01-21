'''################################################################################
        CSCE 206 Homework - 1 , Exercise 1.6
                Compute the growth of money in a bank
                        
                Author:   Sendurr Selvaraj
                Email:    sendurr@hotmail.com
################################################################################'''

principle = 1000.00
year = 3
rate = 5

temp = rate / 100.00
temp1 = (1.00 + temp)** year

output =  principle * temp1

print (" For a amount of " + str(principle) + " euro. After " + str(year) + " years you will have " + str(output) +" euros")




'''################################################################################
        End of Program
################################################################################'''
