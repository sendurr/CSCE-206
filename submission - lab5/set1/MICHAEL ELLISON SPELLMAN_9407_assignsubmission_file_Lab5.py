###Q1
##def printstar(n):
##    print('*')
##    for i in range(n):
##        print('*'),
##    return " "
##printstar(100)
##
###Q2
def main():
    rows = int(input("Enter Number of rows: "))
    stars = int(input("Enter Number of stars: "))
    flag = 0
    for i in range(rows):
        if flag == 0:
            for j in range(stars):
                print('* '),
            print("\n")
            flag = 1
        else:
            for j in range(stars - 1):
                print(' *'),
            print("\n")
            flag = 0

main()
