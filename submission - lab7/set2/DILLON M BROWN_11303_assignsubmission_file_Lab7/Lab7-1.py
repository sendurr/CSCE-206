#Lab 7 Question 1
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('op', help = 'mathematical operator for x and y')
parser.add_argument('x')
parser.add_argument('y')
args = parser.parse_args()

if args.op == '*':
    res = float(args.x)*float(args.y)
    print("%s * %s = %.3f")%(args.x,args.y,res)
elif args.op == '+':
    res = float(args.x)+float(args.y)
    print("%s + %s = %.3f")%(args.x,args.y,res)
elif args.op == '-':
    res = float(args.x)-float(args.y)
    print("%s - %s = %.3f")%(args.x,args.y,res)
elif args.op == '/':
    if float(args.y) == 0:
        print("Error: denominator cannot be 0.")
    else:
        res = float(args.x)/float(args.y)
        print("%s / %s = %.2f")%(args.x,args.y,res)