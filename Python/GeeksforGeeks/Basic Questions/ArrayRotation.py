def rotation(a,d):
	temp = []

	for i in range(d,len(a)):
		temp.append(a[i])

	for j in range(0,d):
		temp.append(a[j])


	return temp

if __name__ == "__main__":
	l = list(map(int,input().split()))
	d = int(input())

	res = rotation(l,d)
	print(res)