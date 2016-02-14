numbers = range(13,999)
def addOddNumbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 1:
            total += num
    print (total)

