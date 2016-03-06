#Rachel Smoak
#Homework 2
#14 February 2016

#Problem 2
import numpy as np #use numpy because it deals with non-integer range things
v0 = 1 #define given constants
g = 9.81
n = 11
endrange = 2*v0/g #define range end and step
stepsize = endrange/n
tlist = np.arange(0,endrange,stepsize) #make a list of t values
ylist = [] #empty list for calculated values
i = 0
while i < len(tlist): #for all of the ts in tlist
	t = tlist[i] #pick the value
	y = v0*t + 0.5*g*t**2 #calculate the answer
	ylist.append(y) #add answer to list
	i+=1 #next element

print '%8s %10s' %('t','y') #print table header, experimented with value until good looking
for t,y in zip(tlist,ylist): #zip lists to get format
	print '%10.2f %10.2f' %(t,y) #print setting to look good
