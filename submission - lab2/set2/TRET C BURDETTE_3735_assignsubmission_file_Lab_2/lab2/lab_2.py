# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 21:24:32 2016

@author: Tret Burdette
"""
print "question one"
t1=("jimmhy",98,35,56)
t2=("jones",89,88,98)
t3=("lucy",99,90,98)

print t2[3]



print "question two"
M1=[[1,1,1],[1,1,1],[1,1,9]]
M2=[[2,2,2],[2,8,2],[2,2,2]]
M3=[M1,M2]
print M3[0][2][2]
print M3[1][1][1]


print "question three"
course=["physics","math","english"]
score=[58,98,98]
for c,s in zip(course,score):
    print (c,s)


print "question four"
city=["Columbia", "Greenville", "Spartanburg", "Charleston", "New York", "London", "Tokyo", "Charlotte", "Orlando","Miami"]
temp=[56,54,54,53,50,54,41,54,67,72]
print "my city=Columbia"
for c,t in zip(city,temp):
    print c,t
