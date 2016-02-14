""" Dillon Brown
Interest Rate Calculator"""

A = float(1000) # Euros
p = float(5)    # annual interest percent
n = 3           # number of years

new_A = A*((1 + (p/100))**n)

print str(new_A) + ' Euros'