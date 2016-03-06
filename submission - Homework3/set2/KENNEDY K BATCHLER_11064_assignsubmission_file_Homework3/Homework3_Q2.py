def sumoddnumbers(numbers):
	total=0
	for number in numbers:
		if(number%2==1):
			total=total+number
	return total

numbers=[]
n=int(input("enter maximum length of a list:"))
while (len(numbers)<n):
	item=input("Enter integer value to the lsit:")
	numbers.append(item)
print("This is your list:",numbers)
print "sum=",sumoddnumbers(numbers)