
x=1
h=0.01
xcoor=[]

for i in range(0,101):  
    xi=h*i
    xcoor.append(x+xi)
xcoor=['%.2f'%elem for elem in xcoor]
print xcoor