# from math import sin,cos [doens't work because pi is not defined]
from math import * #[the * imports all math functions]
x=pi/4
#1_val=sin^2(x) + cos^2(x) [doens't work because you cant call a function that starts with a number, and to obtain the exponent 2 of sin, you must use sin(x)**2 instead of sin^2(x) and the same thing for cos]
val=sin(x)**2 + cos(x)**2
print (val)