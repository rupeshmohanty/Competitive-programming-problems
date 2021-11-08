def checkMonotonic(a):
	flag = True
	for i in range(len(a)-1):
		if a[i] >= a[i+1] or a[i] <= a[i+1]:
			continue
		else:
			flag = False

	return flag

if __name__ == "__main__":
	arr = list(map(int,input().split()))

	res = checkMonotonic(arr)

	if res:
		print("true")
	else:
		print("false")