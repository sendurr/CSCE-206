'''################################################################################
        CSCE 206 Homework - 2 , Exercise P2
                acceleration table
                        
                Author:   Sendurr Selvaraj
                Email:    sendurr@hotmail.com
################################################################################'''




v = 1.0       # Initial velocity of the ball
g = 9.81        # Acceleration of gravity
t = 0.0         # Time
n = 11.0

#define the boundaries for t
end = 2.0*(v / g)
i = 0
step = end/n

print "t \t \t y(t)"
while t < end:    
    y = (v * t) - (0.5 * g * t**2)
    print "%f\t %f" % (t, y)
    t += step 


'''################################################################################
        End of Program
################################################################################'''
