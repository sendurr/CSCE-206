number1=float(raw_input("Please enter a number"))
number2=float(raw_input("Again, enter a different number"))
number3=float(raw_input("Again, enter a different number"))
number4=float(raw_input("Next,enter a different number"))
number5=float(raw_input("Now, enter a different number"))
number6=float(raw_input("Finally, enter a different number"))
numbers=[number1,number2,number3,number4,number5,number6]
minimum=min(numbers)
maximum=max(numbers)
average=float(sum(numbers)/len(numbers))
print "Minimum is %d"%minimum
print "Maximum is %d"%maximum
print average 
print "is the average"