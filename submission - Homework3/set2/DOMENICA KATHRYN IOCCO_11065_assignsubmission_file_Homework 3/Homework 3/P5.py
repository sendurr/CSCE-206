import sys
#import ball_qa.py

#way 1
g1=9.81
v1=float(sys.argv[1])
t1=float(sys.argv[2])
y1=int(v1)*int(t1)-0.5*g1*int(t1)**2
sys.argv=[5,0.8]
print(y1)