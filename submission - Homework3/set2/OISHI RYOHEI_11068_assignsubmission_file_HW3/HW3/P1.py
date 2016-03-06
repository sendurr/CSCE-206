[a,b]=input('input your first position: [ , ]')
[c,d]=input('input your second position: [ , ]')
[e,f]=input('input your third position: [ , ]')

def area(a,b,c,d,e,f):
	return 1/2.0*abs(c*f-e*d-a*f+e*b+a*d-c*b)
print area(a,b,c,d,e,f)
