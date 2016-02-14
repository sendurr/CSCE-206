# Alexis Thompson-Klemish
#

# guassian function
# 
# m = 0
# s = 0
# x = 1

from math import exp,pi,sqrt

m = float(0)
s = float(2)
x = float(1)

val_1 = (( x - m ) / s) ** 2
val_1 = -float(1) / 2 * val_1
val_1 = exp(val_1)

val_2 = 1 / (sqrt(2 * pi) * s)

val_3 = val_1 * val_2

print val_3
