#Rachel Smoak
#28 February 2016

#Lab 6

#Question 1

#Make a program that (i) asks the user for a temperature in Fahrenheit
# degrees and reads the number; (ii) computes the corresponding
# temperature in Celsius degrees; and (iii) prints out the temperature in
# the Celsius scale.

F = float(raw_input("Input a temperature in degrees Fahrenheit:"))
C = (F-32)*5./9.
print "Temperature in degrees Celsius:", C