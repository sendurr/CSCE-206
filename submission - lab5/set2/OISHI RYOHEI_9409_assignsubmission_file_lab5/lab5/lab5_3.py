#lab5_3
def checkprime(num):
		for i in range(2,num):
			if (num % i) == 0:
				print(num,"is not a prime number")
		else:
			print(num,"is a prime number")
       
n=raw_input("enter your integer number: ")
n=int(n)
checkprime(n)