#Q2
import sys

def ftoc(x):
    x = int(x)
    cel = (x-32)*(5./9)
    return cel

print("Temperature Converter using sys.argv")
temp = sys.argv[1:]
for arg in temp:
    try:
        float(arg)
        print(str(arg) + " degrees Fahrenheit")
        print('%.3f degrees Celsius')%(ftoc(float(arg)))
    except ValueError:
        print("%s is not a number")%(arg)