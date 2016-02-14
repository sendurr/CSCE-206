#1
jimmhy = (98,35,56)
jones = (89,88,98)
lucy = (99,90,98)
print jones[2]

#2
M1 = [[1,1,1],[1,1,1],[1,1,9]]
M2 = [[2,2,2],[2,8,2],[2,2,2]]
M3 = [M1,M2]

print M3[0][2][2]
print M3[1][1][1]

#3
scores = {"physics":58,"math":98,"english":98}
for subject in scores:
	print subject,scores[subject]

#4
cityT = {"columbia":65,"florence":66,"beaufort":76,"bluffton":78,"hilton head":67,"greenville":58,"augusta":65,"charlotte":76,"clemson":52,"myrtle beach":58}
for temps in cityT:
	print temps,cityT[temps]
	