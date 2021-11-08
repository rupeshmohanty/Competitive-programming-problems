def reconstruct(a,m):
	for i in range(1,len(a)):
		a[i] = (a[i-1]+1) % m

if __name__ == "__main__":
	arr = list(map(int,input().split()))
	m = int(input())

	reconstruct(arr,m)

	print(arr)