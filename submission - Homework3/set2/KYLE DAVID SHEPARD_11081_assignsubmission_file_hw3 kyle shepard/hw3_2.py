def sumoddnumbers(numbers):
    numbers = [2,5,7,4,8,3,5]
    total = 0
    for num in numbers:
        if num % 2 == 1:
            total += num
    return total

if __name__ == '__main__':
    print sumoddnumbers(numbers)