'''################################################################################
    CSCE 206 Lab7  , Exercise Q1
    Calculator through command line
    
    Author:   Sendurr Selvaraj
    Email:    sendurr@hotmail.com
################################################################################'''

import sys

operator = str(sys.argv[1])
arg1= sys.argv[2]
arg2= sys.argv[3]


try:
    if (operator == '+'):
        result = float(arg1) + float(arg2)

    elif (operator == '-'):
        result = float(arg1) - float(arg2)

    elif (operator == '*'):
        result = float(arg1) * float(arg2)

    elif (operator == '/'):
        if (int(arg2) == 0):
            print ("error: denominator cannot be 0 \n")
            exit()
        else:
            result = float(arg1) / float(arg2)
    else:
        print("error: incorrect operator (use '+' or '-' or '*' or '/')\n")
        exit(1)


    print ( str(arg1)+ " " + operator + " " + str(arg2) + " = " + str(result))

except ValueError:
    print ("Enter numeric arguments!\n")



'''################################################################################
    End of Program
################################################################################'''

