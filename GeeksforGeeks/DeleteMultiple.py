def deleteMultiple(a,r):
	return [x for x in a if x not in r]

if __name__ == '__main__':
	arr = list(map(int,input().split()))
	remove = list(map(int,input().split()))

	res = deleteMultiple(arr,remove)
	print(res)