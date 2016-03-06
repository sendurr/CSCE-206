#Question 2: sumoddnumbers

def sumoddnumber(numbers):
    number= (2,5,7,4,3,8,5)
    total = 0
    for num in number:
        if num % 2 == 1:
            total += num
    return total

print "sum=", sumoddnumber([2,5,7,4,8,3])
