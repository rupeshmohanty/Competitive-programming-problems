def nLargest(l,n):
	l.sort()
	large = []

	for i in range(1,n+1):
		large.append(l[len(l)-i])

	return large


if __name__ == '__main__':
	arr = list(map(int,input().split()))
	N = int(input())
	res = nLargest(arr,N)
	print(res)