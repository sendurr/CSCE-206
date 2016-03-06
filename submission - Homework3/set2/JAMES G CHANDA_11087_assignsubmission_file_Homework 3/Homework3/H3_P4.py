'''Question 4: Prompt the user for input to a formula'''

# v0 = 3; g = 9.81; t = 0.6
# y = v0*t - 0.5*g*t**2
# print y



t = float(raw_input("T=?\n"))
v0 = float(raw_input("v0=?\n"))
g = 9.81

y = v0*t - 0.5*g*t**2
print y