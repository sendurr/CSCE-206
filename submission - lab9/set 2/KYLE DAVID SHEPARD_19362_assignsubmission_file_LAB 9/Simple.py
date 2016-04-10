class Simple:
    def __init__(self,i):
        self.i=i
    def double(self):
        i=self.i
        i=i+i
        return i
s1=Simple(4)
print s1.double()
s2=Simple('Hello')
print s2.double()
s2.i=100
print s2.double()

#I have no clue what the "Try out the code with this" part is expecting the program to do, but heres is a class that replaces i with i+i I think.