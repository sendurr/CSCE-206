# Alexis Thompson-Klemish
#
# initial amount = 1000
# interest rate = 5%
# years = 3

initial_amount = float(1000)
ir = float(5)
years = 3

val = initial_amount * (( 1 + (ir / 100)) ** years)

# round off decimals to 2
val = round(val,2)

print val
