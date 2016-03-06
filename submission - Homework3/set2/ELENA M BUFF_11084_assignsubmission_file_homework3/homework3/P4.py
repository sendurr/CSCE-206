# v0=3; g=9.81; t=0.6
# y=v0*t-0.5*g*t**2
# print y

g=9.81
a=raw_input("t=?\n")
b=raw_input("v0=?\n")
t=int(a)
v0=int(b)

y=v0*t-0.5*g*t**2
print "y= ",y