# P5another
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v",action='store',dest="v0")
parser.add_argument('-t', action='store',dest="t") 
args = parser.parse_args()  
v0=float(args.v0)
g=9.81
t=float(args.t)
y=v0*5-0.5*g*t**2
print y

import argparse
 

args = parser.parse_args()
