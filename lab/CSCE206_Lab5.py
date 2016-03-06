'''################################################################################
        CSCE 206 LAB - 5
                Lab -5 : Using functions
                        
                Author:   Sendurr Selvaraj
                Email:    sendurr@hotmail.com
################################################################################'''
'''################################################################################
        printstar
               Prints n no of *
################################################################################'''

def printstar(n):

    for i in range(1,n+1):
        print("*"),
    #print("\n")


'''################################################################################
        End of method
################################################################################'''

'''################################################################################
        printstarx
               Prints n no of * with rows equal to 'row'
################################################################################'''

def printstarx(n , row=1):

    for i in range(1,row+1):
        for j in range(1,n+1):
            print("*"),
        print("\n")

    print ("Now printing another way using printstar(n) within printstarx(n,row)\n")

    for i in range(1,row+1):
        printstar(n)
        print("\n")    

'''################################################################################
        End of method
################################################################################'''
'''################################################################################
        printstarx
               Prints n no of * with rows equal to 'row'
################################################################################'''

def checkprime(n):

    if n==1:
        return False

    for x in range(2,n):
        if (n%x==0):
            return False
    return True


'''################################################################################
        End of method
################################################################################'''

# Q1: 
# define a function called printstar(n), which will print n number of '*' on a single line.
#  (Hint, add a ',' at end of print statement will keep next print to output at same line)
# test your function by calling

# printstar(1)
# printstar(10)
# printstar(100)

# Q2: 
# define a function call printstarx, which has two parameters.
# n parameter specifies how many stars to print on each row
# row parameter specify how many rows to print stars
# the row parameter should have a default value as 1.
# so this function will print a couple of rows, each row composed of n stars.  
# You can call printstar(n) function in Q1 to work out this problem. 


# test your function by calling

# printstarx(10)  #which should print 1 row with 10 stars
# printstarx(10,5)# should print 5 rows, each with 10 stars

print ("Printing Question1 Answers \n")
print ("Calling function printstar(1)")
printstar(1)
print ("\nCalling function printstar(10)")
printstar(10)
print ("\nCalling function printstar(100)")
printstar(100)


print ("\nPrinting Question 2 Answers \n")

print ("Calling function printstarx(10)")
printstarx(10)

print ("Calling function printstarx(10,5)")
printstarx(10,5)


# def checkprime(n):
#     #your code here
#     #hint, you just need to check if there is any number x from 2 #to n-1 that makes n%x==0. if so, it is not a prime, return #false. otherwise return true.

# test your function by:

# print checkprime(3)  #shoud get true
# print checkprime(255) #should get false

print ("Printing Question 3 Answers \n")
print ("Checking prime for  checkprime(3) \n")
print checkprime(1)
print ("Checking prime for  checkprime(225) \n")
print checkprime(225)



'''################################################################################
        End of Program
################################################################################'''
