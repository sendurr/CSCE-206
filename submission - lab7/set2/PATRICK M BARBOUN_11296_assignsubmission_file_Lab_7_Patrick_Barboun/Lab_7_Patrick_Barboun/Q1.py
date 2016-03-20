import sys as sys

if sys.argv[1]=='.':
	print float(sys.argv[2])*float(sys.argv[3])
if sys.argv[1]=='+':
	print float(sys.argv[2])+float(sys.argv[3])
if sys.argv[1]=='-':
	print float(sys.argv[2])-float(sys.argv[3])
if sys.argv[1]=='/' and int(sys.argv[3])!=0:
	print float(sys.argv[2])/float(sys.argv[3])
if int(sys.argv[3])==0 and sys.argv[1]=='/':
	print 'Error: cannot divide by zero'