args = parser.parse_args()
g = 9.81

try:
	v0 = float(args.v0)
	t = float(args.t)

except:
	print 'Initial velocity and time parameters were not specified in Command line'
	v0 = float(raw_input('Enter v0:'))
	t = float(raw_input('Enter t:'))

y = ((v0 * t) - (.5 * g * t**2))

print 'y =',y



