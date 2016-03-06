
import math

def sumoddnumber (numbers):
	total=0
	for num in numbers:
		if num %2==1:
			total+=num
		return total

if_name_=='_main_'
print 'sum=',sumoddnumber(numbers=[2,5,2.3,5,10,4.2])