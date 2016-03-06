# #P3
# import sys
# numbers=[]
# for j in sys.argv:
# 	numbers.append(float(j))

# def minmaxave(numbers):
# 	sum=0
# 	for i in numbers:
# 		sum=sum+float(i)
# 	average = sum/len(numbers)
# 	print "the max value is %d"%max(numbers)
# 	print "The minimum value is %f"%min(numbers)
# 	print "The average is %f"%average
# minmaxave(numbers)

n=input("how many numbers do you have?: ")
x=[]
for i in range(n):
    x.append(float(input("value of %dth number?"%(i+1))))
def minmaxave(x):
	average=sum(x)/len(x)
	print "minimum value is %d"%(min(x))
	print "maximum vlaue is %d"%(max(x))
	print "average is %f"%average
minmaxave(x)


