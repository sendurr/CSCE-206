# Name: Lucke Oliveira Luz			Assignment: Lab 5          Exercise: 3

def checkprime(n):
	if n == 2:
		return "true"
	else:
		x = 2
		while x < n:
			if n%x == 0:
				return "false"
			elif x < n-1:
				x += 1
			else:
				return "true"

print checkprime(3)
print checkprime(255)