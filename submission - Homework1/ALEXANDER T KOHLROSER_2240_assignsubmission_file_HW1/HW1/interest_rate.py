from decimal import Decimal, ROUND_HALF_UP
#allows the removal of excess decimal places and also rounds up

A = 1000
p = 0.05
n = 3
#given variables

Growth = Decimal(A * (1 + p / 100) ** (n))
#calculation and conversion to decimal format

output = round (Growth,2)
#rounding operation

print ("The investment has grown to ")
print (output)
print ("Euros")
#printing with words