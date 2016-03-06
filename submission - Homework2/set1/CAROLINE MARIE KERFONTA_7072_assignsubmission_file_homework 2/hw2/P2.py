v = 5.0       
g = 9.81  
t = 0.0   

end = 2.0*(v / g)
i = 0
step = end/11

print ("t\t\ty(t)")
while t < end:    
    y = (v * t) - (0.5 * g * t**2)
    print ("%f\t%f"% (t, y))
    t += step 