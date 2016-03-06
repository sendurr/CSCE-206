
import argparse
parser= argparse.ArgumentParser()
parser.add_argument('-f', action='store', dest='f', default=0, help="temp in farenheit")
parser.add_argument('-c', action='store', dest='c', default=0, help="temp in celcius")
args=parser.parse_args()
# print args.f
# print args.c

f=float(args.f)
c=float(args.c)
C=(f-32)*5/9
F=(c*9/5)+32
print'Output Temperature in Celcius =',C
print "Output Temperature in Farenheit =",F

