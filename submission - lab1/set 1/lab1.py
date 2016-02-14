#1
print ("1.")
i=2.33
j=-2
name="32233"
name1='I am a boy'
print (i,' ',j,' ',name,' ',name1)
print ()

#2
print ("2.")
array1=3,4.0,34,-5,23
print ("numbers of even indexes:",array1[0],' ',array1[2],' ',array1[4])
print ()

#3
print ("3.")
words="good", "very good", "excellent"
print (words[0],' ',words[2])
print ()

#4
print ("4.")
m=[1,2,3],[4,5,6],[7,8,9]
for x in m:
	print (x)
print ("center number =",m[1][1])
print ()

#terminal
value=input("give me a number:")
print (value)
#this code works in Terminal, but not in Sublime
