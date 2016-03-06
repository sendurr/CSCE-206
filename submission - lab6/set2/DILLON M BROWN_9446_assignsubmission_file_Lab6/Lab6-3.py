import argparse
def ftoc(x):
    x = float(x)
    cel = (x-32)*(5.0/9)
    return cel
def ctof(x):
    x = float(x)
    fah = ((9.0/5)*x) + 32
    return fah

parser = argparse.ArgumentParser()
parser.add_argument("deg", help="the temperature in degrees Fahrenheit")
parser.add_argument("unit", help ="f or c")
args = parser.parse_args()
print args.deg, args.unit
unit = args.unit

print("Temperature Converter using argparse")
try:
    float(args.deg)
except ValueError:
    print("Inputted argument '" + str(args.deg) + "' not a number")
if unit.lower() == 'f':
    print('input: ' + str(args.deg) + " degree (F)")
    print('output: ' + '%.2f degree (C)')%(ftoc(float(args.deg)))
if unit.lower() == 'c':
    print('input: ' + str(args.deg) + " degree (C)")
    print('output: ' + '%.2f degree (F)')%(ctof(args.deg))
else:
    print("Error: specify Fahrenheit (f) or Celsius (c)")