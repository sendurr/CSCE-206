import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-F', action='store', dest='F',default='32', help='Degrees Farhenheit')
args = parser.parse_args()

F = eval(args.F)

print (F-32.)*5./9.


