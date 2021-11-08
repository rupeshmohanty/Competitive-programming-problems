def interchange(a):
	temp = a[0]
	a[0] = a[len(a)-1]
	a[len(a)-1] = temp


l = list(map(int,input().split()))
interchange(l)
print(l)
