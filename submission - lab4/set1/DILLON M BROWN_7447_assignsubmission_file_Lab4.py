##Lab4 Number 1: Work with A List.
#Dillon Brown

def list_write(x):
    for a in x:
        print a


primes = [2,3,5,7,11,13]
p = 17

list_write(primes)
primes.append(p)
list_write(primes)
print '------------------'
##Lab4 Number 2: compute a mathematical Sum

def forloopsum(M):
    s = 0
    for x in range(1,M):
        s+=(1.0/x)
    return s
def whileloopsum(M):
    s = 0
    k = 1
    while k<M:
        s+= 1.0/k
        k+=1
    return s

print forloopsum(100)
print whileloopsum(100)
print '------------------'
##Lab 4 Number 3: Store matrix M and calculate sum of
#numbers on boundary (I assume this means numbers represented
# by x
#
#   x x x
#   x o x
#   x x x

M = [[1,2,3],[4,5,6],[7,8,9]]
s = 0

for a in M:
    if M.index(a) == 0 or M.index(a) == len(M)-1:
        s = s + sum(a)
    else:
        for x in a:
            if a.index(x) == 0 or a.index(x) == len(a)-1:
                s = s + x
print s

