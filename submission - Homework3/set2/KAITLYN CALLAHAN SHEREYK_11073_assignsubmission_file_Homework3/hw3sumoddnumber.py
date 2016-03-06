def sumoddnumber(int_list):
    odd_total = 0
    for num in int_list:
        num = int(num)
        if num % 2 != 0:
            odd_total += num
    return odd_total

def main():
    print 'sum = ', sumoddnumber([2,5,7,4,8,3,5])

if __name__ == '__main__':
    main()







