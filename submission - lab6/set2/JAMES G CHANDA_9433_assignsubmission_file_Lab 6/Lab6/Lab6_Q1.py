'''Question 1: write a program that takes input from user by keyboard:

Make a program that (i) asks the user for a temperature in Fahrenheit
degrees and reads the number; (ii) computes the correspodning
temperature in Celsius degrees; and (iii) prints out the temperature in
the Celsius scale. Name of program file: f2c_qa1.py'''

def FtoC(c):
    return (c-32)*5./9.

input = raw_input("Give me the temperature in Fahrenheit = \n")
print "The temperature in Celsius is %d" % FtoC(int(input))
