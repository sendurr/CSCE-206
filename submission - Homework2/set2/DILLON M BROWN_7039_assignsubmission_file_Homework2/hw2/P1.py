#P1: Generate first 1000 numbers of series n = n(i-1) + n(i-2)
#for i>2

result = [0,1]

for i in range(2,1000):
    result.append(result[i-2]+result[i-1])
print result