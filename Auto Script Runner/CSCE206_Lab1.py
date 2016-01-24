'''################################################################################
        CSCE 206 LAB - 1
                Lab -1 : Learn to store information into variables - Solution
                        
                Author:   Sendurr Selvaraj
                Email:    sendurr@hotmail.com
################################################################################'''

# Exercise 1 : Store  2.33, -2, "32233", 'I am a boy' into 4 different variables
# and then print the variables out

x_float = 2.233
y_int = -2
z_string1 = "32233"
z_string2 = "I am a boy"

print "Printing results of exercise 1 \n"
print x_float
print y_int
print z_string1
print z_string2
print "exercise 1 completed \n \n"

# Exercise 2 :store a list of numbers into variable called  array1 and print 
# out the numbers of even indexes 3,4.0,34,-5,23

print "Printing results of exercise 2 \n"

array1 = [3,4.0,34,-5,23]

arr_len = len(array1)
i=0
while(i<arr_len):
        print "The value of array1 with index " + str(i) + " is " + str(array1[i])
        i=i+2
print "exercise 2 completed \n \n"

# Exercise 3 :Store a list of strings into a variable and print out first and last items.
# "good","very good","excellent"
        
string_list =["good","very good","excellent"]
        
print "Printing results of exercise 3 \n"
print "Printing the first element  = " + string_list[0]
print "Printing the last element  = " + string_list[-1]

print "exercise 3 completed \n \n"

# Exercise 4 : Store a matrix of numbers into a variable m
# 1 2 3
# 4 5 6
# 7 8 9
# print the center number using m with indexes

my_array = [[1,2,3],[4,5,6],[7,8,9]]
print "Printing results of exercise 4 \n"

print "The value of array with index 0 , 1 is " + str(my_array[0][1])
print "The value of array with index 1 , 1 is " + str(my_array[1][1])
print "The value of array with index 2 , 1 is " + str(my_array[2][1])

print "exercise 4 completed \n \n"


'''################################################################################
        End of Program
################################################################################'''