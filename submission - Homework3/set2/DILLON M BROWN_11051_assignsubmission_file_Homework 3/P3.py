def minmaxave(numbers):
    return max(numbers), min(numbers), sum(test)/float(len(test))

test = [3,5,2.3,5,10,4.2]
print minmaxave(test)