"""2) store a list of numbers into variable
 called  array1 and print out the numbers of even indexes
 Dillon Brown"""

array1 = [3,4.0,34,-5,23]

for x in range(0,len(array1)):
    if x%2 == 0:
        print array1[x]