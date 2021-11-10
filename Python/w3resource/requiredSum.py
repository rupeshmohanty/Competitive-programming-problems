def requiredSum(a,b,c,t):
	res = []

	for i in a:
		for j in b:
			for k in c:
				s = 0

				s += i + j + k

				if s == t:
					res.append((i,j,k))

	return res

if __name__ == "__main__":
	l1 = list(map(int,input().split()))
	l2 = list(map(int,input().split()))
	l3 = list(map(int,input().split()))
	target = int(input())

	res = requiredSum(l1,l2,l3,target)
	print(res)