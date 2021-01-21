def findRemainder(l,pos):
	mul = 1

	for i in range(len(l)):
		mul = mul*l[i]

	res = mul % pos

	return res

if __name__ == '__main__':
	arr = list(map(int,input().split()))
	n = int(input())

	res = findRemainder(arr,n)
	print(res)