#Lab6 Q1

def ftoc(x):
    x = int(x)
    cel = (x-32)*(5./9)
    return cel

print("Type stop to stop")
while True:
    temp = raw_input("Input Temperature in Degrees Fahrenheit: ")
    if temp.lower() == 'stop':
        break
    else:
        try:
            float(temp)
            print(str(temp) + " degrees Fahrenheit")
            print('%.3f degrees Celsius')%(ftoc(float(temp)))
        except ValueError:
            print("That's not a number")
