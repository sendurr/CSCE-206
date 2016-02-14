"""1. store  2.33, -2, "32233", 'I am a boy' into 4 different variables and then print the variables out"""

x = "Question 1"
print (x)
my_var = 2.33
my_var2 = -2
my_var3 = 32233
my_var4 = "I am a boy"
print (my_var)
print (my_var2)
print (my_var3)
print (my_var4)
print (" ")

"""2. store a list of numbers into variable called  array1 and print out the numbers of even indexes
3,4.0,34,-5,23"""

x = "Question 2"
print (x)
my_list = [3, 4.0, 34, -5, 23]
for i in range(len(my_list)):
	if i%2 == 0:
		print i, my_list[i]
print (" ")

"""3. store a list of strings into a variable and print out first and last items.
"good","very good", "excellent"""

x = "Question 3"
print (x)
my_string = ["good", "very good", "excellent"]
print my_string[0]
print my_string[-1]
print (" ")

"""4. store a matrix of numbers into a variable m
1 2 3
4 5 6
7 8 9

Print the center number using m with indexes"""

x = "Question 4"
print (x)

m = [[1,2,3], 
	 [4,5,6], 
	 [7,8,9]]
print m[1][1]

