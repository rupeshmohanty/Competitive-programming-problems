def swapAnyTwo(l,p1,p2):
	temp = 0

	#swapping the elements placed in that position
	temp = l[p1]
	l[p1] = l[p2]
	l[p2] = temp

	return l

if __name__ == '__main__':
	arr = list(map(int,input().split()))
	pos1 = int(input())
	pos2 = int(input())
	res = swapAnyTwo(arr,pos1,pos2)
	print(res)