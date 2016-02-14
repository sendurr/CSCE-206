# Author: Daniel Harper
# Assignment: Homework 1 - interest_rate.py
# Original Date: 1/21/2016
# Last Updated:  1/21/2016
# Written using Python 3.4.3.7
# All rights reserved
# Description: Accomplish tasks outlined in the assignment document
#####################################################################
# Importation Section################################################
# from math import * # basic math library

# Body Section#######################################################

# FUNCTION:growth(A,p,n)---------------------------------------------
# Description: output the growth due to interest of a sum of money
# Input Parameters:
#	A : initial amount of money
#	p : bank's interest rate in percent per year (example: 5% = 5.0)
#	n : number of years A is allowed to sit in the account
def growth(A,p,n):
	result = A * (1 + (p / 100.0))**n
	return result
#--------------------------------------------------------------------

x = 1000.00
y = 5.0
z = 3

print("%0.2f"%(growth(x,y,z)))
