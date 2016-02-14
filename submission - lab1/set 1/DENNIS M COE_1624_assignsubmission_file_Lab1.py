x = 2.33
d = -2
s = 32233
l = "I am a boy"
print (x, d, s, l)

array1 = [3, 4.0, 34, -5, 23]

def even_ind(ar):
	for i in range(0, len(ar)):
		if i % 2 == 0:
			print (ar[i])

even_ind(array1)

j = ['good', 'very good', 'excellent']
print (j[0])
print (j[len(j) - 1])


from numpy import matrix
m = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

print (m[1][1])
