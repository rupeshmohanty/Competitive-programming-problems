def swapList(l):
	temp = 0
	n = len(l)
	# swapping the first and last elements!
	temp = l[0]
	l[0] = l[n-1]
	l[n-1] = temp

	return l 

if __name__ == '__main__':
	arr = list(map(int,input().split()))
	res = swapList(arr)
	print(res)