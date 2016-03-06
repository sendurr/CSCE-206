
n=int(raw_input("how many roots:"))

r=[]
for i in range(n):
	r.append(float(raw_input("value of %dth root?"%(i+1))))

r1 = 0
r2 = 0
r3 = 0

x = int(raw_input("what is x, *hint p(x)=(x-r1)*(x-r2)...(x-r_n-1_)*(x-r_n_) is the equation*?:"))

print (r)
formula = r1+r2+r3

for i in range(n):
	print ("r%d"%(i+1)+" = r["+str(i)+"]")
	exec("r%d"%(i+1)+" = r["+str(i)+"]")



print ("answer=",eval('(x-r1)*(x-r2)*(x-r3)'))

