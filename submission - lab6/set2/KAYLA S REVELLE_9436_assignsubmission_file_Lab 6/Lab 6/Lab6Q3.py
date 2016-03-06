import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', action='store', dest='f',default=0, help='Farenheit Temperature: ')
parser.add_argument('-c', action='store', dest='c',default=0, help='Celsius Temperature: ')
args = parser.parse_args()


f=float(args.f)
c=float(args.c)
F=(f-32)*5/9
C=(c*9/5)+32

print (F,"degree F")
print (C, "degree C")