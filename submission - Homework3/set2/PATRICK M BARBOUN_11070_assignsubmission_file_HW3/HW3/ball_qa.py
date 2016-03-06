V0 = float(raw_input("Initial Velocity in meters?"))
t = float(raw_input("Time in seconds?"))
g = 9.81
y = V0*t-.5*g*t**2
print float(y)