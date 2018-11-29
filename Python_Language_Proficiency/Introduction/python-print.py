import sys
n=int(raw_input())
def printf(hm, *varargs):
	sys.stdout.write(hm %varargs)
for k in range(1,n+1):
	printf(str(k))
'''
or 
for k in range(1,n+1):
   print(k,end='')
'''
