def cumulativeSum(l):
	sum = 0
	cm = []
	for i in range(len(l)):
		sum = sum + l[i]
		cm.append(sum)

	return cm

if __name__ == '__main__':
	arr = list(map(int,input().split()))

	res = cumulativeSum(arr)
	print(res)