'''################################################################################
        CSCE 206 Lab - 4 , Exercise P3
                Matrix boundary
                        
                Author:   Sendurr Selvaraj
                Email:    sendurr@hotmail.com
################################################################################'''




mat = [[1 , 2 ,3 ],[4 , 5 ,6 ],[7 , 8 ,9]]
sum=0

for i in range(0,3):
        for j in range(0,3):
                if(i==0 or i==2):
                        sum = sum + mat[i][j]
                        print str(mat[i][j])
                if (i==1):
                        if(j==0 or j==2):
                                sum = sum + mat[i][j]
                                print str(mat[i][j])

print ("The sum of boundary numbers is "+ str(sum)) 


'''################################################################################
        End of Program
################################################################################'''
