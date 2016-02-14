'''################################################################################
        CSCE 206 Lab - 4 , Exercise P2
                Compute a mathematical sum
                        
                Author:   Sendurr Selvaraj
                Email:    sendurr@hotmail.com
################################################################################'''




sum=0.0
m=5
k=1


while (k<=m):
	sum=sum +	(1.0/k)
	k=k+1

print("Printing sum using while loop for M=" +str(m) + ", sum = " + str(sum) + "\n")

sum=0.0

for k in range (1 ,m+1):
	sum=sum +	(1.0/k)

print("Printing sum using for loop for M=" +str(m) + ", sum = " + str(sum) + "\n")



'''################################################################################
        End of Program
################################################################################'''
