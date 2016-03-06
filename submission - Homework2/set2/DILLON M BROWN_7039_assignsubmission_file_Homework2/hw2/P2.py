#generate table of function values over a range of inputs

v0 = 1.0
g=9.81
n=11
steps = []
results = []
def f(t):
    result = v0*t - 0.5*g*(t**2)
    return result

def frange(start,stop,step):
    i = start
    while i<stop:
        yield i
        i += step

for t in frange(0,(2*v0/g),(2*v0/(g*n))):
    steps.append(t)
    results.append(f(t))
print '%4s %12s' %('t', 'f(t)')
for x in range(0,len(steps)):
    print '%7.5f %10.5f' %(steps[x],results[x])