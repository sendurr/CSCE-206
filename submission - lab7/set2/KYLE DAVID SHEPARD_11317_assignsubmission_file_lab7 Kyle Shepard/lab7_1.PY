def add(x,y):
   return x+y
def sub(x,y):
   return x-y
def mult(x,y):
   return x*y
def div(x,y):
   return x/y
operation = input("add, sub, mult, div: ")
n1=int(input("first number: "))
n2=int(input("second number: "))
if operation=='add':
   print add(n1,n2)
if operation=='sub':
   print sub(n1,n2)
if operation=='mult':
   print mult(n1,n2)
if operation=='div':
   print div(n1,n2)

# I cant seem to figure out why I cant get it to print the results