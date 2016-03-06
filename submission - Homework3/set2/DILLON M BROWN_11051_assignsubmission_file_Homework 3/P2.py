def sumoddnumber(numbers):
    s = 0
    for x in numbers:
        if x%2 != 0:
            s+=x
    return s

test = [2,5,7,4,8,3,5]
print "sum = %d"%(sumoddnumber(test))