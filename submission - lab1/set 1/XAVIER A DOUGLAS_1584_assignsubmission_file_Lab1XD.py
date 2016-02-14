#X'Avier Douglas Lab 1
from math import *

#1
print ("#1")
a = 2.33
print ("a =",a)
b = -2
print ("b =",b)
c = "32233"
print ("c =",c)
d = 'I am a boy'
print ("d =",d)

#2
print ("#2")
array1 = [3,4.0,34,-5,23]
even = 0
for x in array1:
	if x %2 == 0:
		even +=1
print ("even = ", even)

#3
print ("#3")
G = ["good","very good", "excellent"]
print ("First Item =",G[0])
print ("Second Item =", G[-1])

#4
print ("#4")
m = [[1,2,3],[4,5,6],[7,8,9]]
print ("Matrix M = ")
print(m[0])
print(m[1])
print(m[2])

print("Center Number =", m[1][1])

value = input("give me a number:")
print (value)