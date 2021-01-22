def findDuplicates(l):
	dup = []
	for i in range(len(l)):
		count = 0
		temp = l[i]
		for j in range(i,len(l)):
			if l[j] == l[i] and l[i] not in dup:
				count = count + 1
		if(count > 1):
			dup.append(l[i])

	return dup

# main function
if __name__ == '__main__':
	arr = list(map(int,input().split()))

	res = findDuplicates(arr)
	print(res)

# This code is contributed by Rupesh Chandra Mohanty
