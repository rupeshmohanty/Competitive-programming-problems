def triplets(l):
	res = []

	for i in range(len(l)-2):
		if l[i] + l[i+1] + l[i+2] == 0:
			res.append((l[i],l[i+1],l[i+2]))

	return res

if __name__ == "__main__":
	lt = list(map(int,input().split()))
	r = triplets(lt)

	print(r)