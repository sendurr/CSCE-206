def f(v0,t,g=9.81):
    return v0*t - 0.5*g*t**2

print("Please enter initial velocity: ")
while True:
    v = raw_input('>')
    try:
        float(v)
        break
    except:
        print "Please enter initial velocity: "
print("Now enter time: ")
while True:
    ti = raw_input('>')
    try:
        float(ti)
        break
    except:
        print("Now enter time: ")
print f(float(v),float(ti))