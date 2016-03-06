ef sumOddNumbers(numbers):
    return sum(num for num in numbers if num % 2 == 1)

print ("sum=", sumOddNumbers([2,5,7,4,8,3,5]))