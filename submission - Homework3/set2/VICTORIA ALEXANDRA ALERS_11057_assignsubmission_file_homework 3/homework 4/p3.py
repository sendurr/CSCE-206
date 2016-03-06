def ave(numbers):
 	sumofnumbers=0
 	for z in numbers:
 		sumofnumbers+= z
 		average=float((sumofnumbers))/len(numbers)
 	return(average)
def mini(numbers):
	minim=numbers[0]
	maxim=numbers[0]
	for x in numbers:
		if x < minim:
			minim=x
		if x > maxim:
			maxim=x
	return (maxim, minim)
def minmaxave(numbers):
	return(mini(numbers),ave(numbers))
print (minmaxave([3,5,2.3,5,10,4.2]))