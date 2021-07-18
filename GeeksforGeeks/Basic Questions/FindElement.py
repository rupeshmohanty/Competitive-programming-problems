def findElement(l,n):
	for i in range(len(l)):
		if(l[i] == n):
			return True
	else:
		return False

if __name__ == '__main__':
	arr = list(map(int,input().split()))
	num = int(input())

	res = findElement(arr,num)
	print(res)