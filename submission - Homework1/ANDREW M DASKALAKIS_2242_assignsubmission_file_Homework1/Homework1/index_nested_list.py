from numpy import matrix

q = [['a','b','c'],['d','e','f'],['g','h']]

print q[0][0] 						# a
print q[1]    						# second row
print q[len(q)-1][len(q[0])-2]		# last element
print q[1][0]						# d

print q[-1][-2]  					# This answer is g because using negative numbers just goes in reverse. q[-1] is the list ['g','h'] from there we can get q[-1][-2] starting with
									# q[-1][0] = g then g[-1][-1] = h, after that it goes back around so q[-1][-2] = g again.