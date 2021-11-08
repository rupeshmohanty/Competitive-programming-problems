def multiplyRemainder(a,n):
	mul = 1

	for i in range(len(a)):
		mul *= a[i]

	return mul % n

if __name__ == "__main__":
	arr = list(map(int,input().split()))
	num = int(input())

	res = multiplyRemainder(arr,num)

	print(res)