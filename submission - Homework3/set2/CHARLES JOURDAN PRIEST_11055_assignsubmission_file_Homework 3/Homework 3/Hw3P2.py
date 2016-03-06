def sumOddNumbers(numbers):
    return sum(num for num in numbers if num % 2 == 1)

print ("sum=", sumOddNumbers([2,5,7,4,8,3,5]))

#The question states that the readout to the above statement should be 15
#This is not true, 7 + 5 + 3 + 5 = 20, not 15