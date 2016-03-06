
def sumoddnumber(numbers):
    sum_odd = 0
    for i in numbers:
        if i%2:
            sum_odd += i
    return (sum_odd)
print("sum=",sumoddnumber([2,5,7,4,8,3,5]))
